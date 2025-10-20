#!/usr/bin/env python3
"""
PROBLEMA INTEGRADOR DE PRÁCTICA
Sistema de Gestión de Restaurante

Nombre: Juan Pablo Ruiz Trujillo
Fecha: 20/10/2025
"""
# ==========================================================
# EXCEPCIONES PERSONALIZADAS
# ==========================================================

class ErrorRestaurante(Exception):
    pass


class PlatoNoEncontrado(ErrorRestaurante):
    def __init__(self, codigo_plato):
        super().__init__(f"Plato con código '{codigo_plato}' no encontrado.")


class MesaNoDisponible(ErrorRestaurante):
    def __init__(self, numero_mesa):
        super().__init__(f"Mesa {numero_mesa} no está disponible en este momento.")


class CapacidadExcedida(ErrorRestaurante):
    def __init__(self, numero_mesa, capacidad, comensales):
        super().__init__(f"Mesa {numero_mesa} tiene capacidad {capacidad}, no {comensales} comensales.")


class PedidoInvalido(ErrorRestaurante):
    def __init__(self, razon):
        super().__init__(f"Pedido inválido: {razon}")

class SistemaRestaurante:
    def __init__(self, num_mesas=5, tasa_impuesto=0.16, propina_sugerida=0.1):
        self.menu = {}
        self.mesas = {}
        self.pedidos = {}
        self.contador_ventas = {}
        self._next_pedido_id = 1
        self.tasa_impuesto = tasa_impuesto
        self.propina_sugerida = propina_sugerida
        self._cargar_menu_interno(num_mesas)

    # ---------------- MENÚ ----------------
    def _cargar_menu_interno(self, num_mesas):
        # Crear mesas vacías
        for i in range(1, num_mesas + 1):
            self.mesas[i] = {"capacidad": 4, "ocupada": False, "pedido": None}

        # Cargar menú interno
        platos = [
            ("P01", "Hamburguesa", "Comida rápida", 18.0),
            ("P02", "Pizza", "Comida rápida", 20.0),
            ("P03", "Ensalada César", "Ensaladas", 15.0),
            ("P04", "Pasta Alfredo", "Pastas", 22.0),
            ("P05", "Limonada", "Bebidas", 8.0),
            ("P06", "Jugo Natural", "Bebidas", 9.0),
            ("P07", "Helado", "Postres", 10.0),
            ("P08", "Café", "Bebidas", 6.0),
            ("P09", "Sopa del Día", "Entradas", 12.0),
            ("P10", "Arroz con Pollo", "Plato fuerte", 25.0)
        ]
        for codigo, nombre, categoria, precio in platos:
            self.menu[codigo] = {
                "nombre": nombre,
                "categoria": categoria,
                "precio": precio,
                "disponible": True
            }
            self.contador_ventas[codigo] = 0

    def mostrar_menu(self):
        print("\n=== MENÚ DEL RESTAURANTE ===")
        for c, d in self.menu.items():
            if d["disponible"]:
                print(f"{c}: {d['nombre']} - ${d['precio']} ({d['categoria']})")

    def reservar_mesa(self, numero, comensales):
        if numero not in self.mesas:
            raise ValueError("Mesa no existe.")
        mesa = self.mesas[numero]
        if mesa["ocupada"]:
            raise MesaNoDisponible(numero)
        if comensales > mesa["capacidad"]:
            raise CapacidadExcedida(numero, mesa["capacidad"], comensales)

        mesa["ocupada"] = True
        print(f"Mesa {numero} reservada para {comensales} persona(s).")

    def liberar_mesa(self, numero):
        if numero not in self.mesas:
            raise ValueError("Mesa no existe.")
        if not self.mesas[numero]["ocupada"]:
            print(f"Mesa {numero} ya está libre.")
            return
        self.mesas[numero]["ocupada"] = False
        self.mesas[numero]["pedido"] = None
        print(f"🪑 Mesa {numero} liberada.")

    def crear_pedido(self, numero_mesa):
        if numero_mesa not in self.mesas:
            raise ValueError("Mesa no existe.")
        if not self.mesas[numero_mesa]["ocupada"]:
            raise ValueError("Mesa no está ocupada.")
        pid = f"PED{self._next_pedido_id:03d}"
        self._next_pedido_id += 1
        self.pedidos[pid] = {
            "mesa": numero_mesa,
            "items": [],
            "pagado": False
        }
        self.mesas[numero_mesa]["pedido"] = pid
        print(f"Pedido creado con ID: {pid}")
        return pid

    def agregar_item(self, id_pedido, codigo_plato, cantidad):
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("no existe.")
        if codigo_plato not in self.menu:
            raise PlatoNoEncontrado(codigo_plato)
        if not self.menu[codigo_plato]["disponible"]:
            raise PedidoInvalido("plato no disponible.")
        if cantidad < 1:
            raise PedidoInvalido("cantidad inválida.")

        pedido = self.pedidos[id_pedido]
        pedido["items"].append((codigo_plato, cantidad))
        self.contador_ventas[codigo_plato] += cantidad
        print(f"{cantidad}x {self.menu[codigo_plato]['nombre']} agregado al pedido.")

    def calcular_total(self, id_pedido, propina_porcentaje=None):
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("pedido no encontrado.")
        pedido = self.pedidos[id_pedido]
        subtotal = sum(self.menu[c]["precio"] * cant for c, cant in pedido["items"])
        impuesto = subtotal * self.tasa_impuesto
        propina = subtotal * (propina_porcentaje or self.propina_sugerida)
        total = subtotal + impuesto + propina
        return {"subtotal": subtotal, "impuesto": impuesto, "propina": propina, "total": total}

    def pagar_pedido(self, id_pedido):
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("pedido no encontrado.")
        pedido = self.pedidos[id_pedido]
        if pedido["pagado"]:
            raise PedidoInvalido("ya fue pagado.")
        totales = self.calcular_total(id_pedido)
        pedido["pagado"] = True
        self.liberar_mesa(pedido["mesa"])
        print(f"Pedido {id_pedido} pagado. Total: ${totales['total']:.2f}")
        return totales

    def platos_mas_vendidos(self, n=5):
        lista = sorted(self.contador_ventas.items(), key=lambda x: x[1], reverse=True)
        print("\nPlatos más vendidos:")
        for codigo, cantidad in lista[:n]:
            print(f" - {self.menu[codigo]['nombre']}: {cantidad} vendidos")

def menu():
    restaurante = SistemaRestaurante()

    while True:
        print("\n=== SISTEMA DE RESTAURANTE ===")
        print("1. Ver menú")
        print("2. Reservar mesa")
        print("3. Crear pedido")
        print("4. Agregar item al pedido")
        print("5. Pagar pedido")
        print("6. Ver platos más vendidos")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                restaurante.mostrar_menu()

            elif opcion == "2":
                mesa = int(input("Número de mesa: "))
                com = int(input("Número de comensales: "))
                restaurante.reservar_mesa(mesa, com)

            elif opcion == "3":
                mesa = int(input("Número de mesa: "))
                restaurante.crear_pedido(mesa)

            elif opcion == "4":
                pid = input("ID del pedido: ")
                cod = input("Código del plato: ")
                cant = int(input("Cantidad: "))
                restaurante.agregar_item(pid, cod, cant)

            elif opcion == "5":
                pid = input("ID del pedido: ")
                restaurante.pagar_pedido(pid)

            elif opcion == "6":
                restaurante.platos_mas_vendidos()

            elif opcion == "7":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida.")

        except Exception as e:
            print(e)

if __name__ == "__main__":
    menu()
