#!/usr/bin/env python3
"""
SISTEMA DE BIBLIOTECA - SIN IMPORTAR NADA
Fechas reemplazadas por contadores simples
Estudiante: Juan Pablo Ruiz Trujillo
Fecha: 20/10/2025
"""
from datetime import datetime, timedelta

# ===================== EXCEPCIONES =====================

class ErrorBiblioteca(Exception):
    pass


class LibroNoEncontrado(ErrorBiblioteca):
    def __init__(self, isbn):
        super().__init__(f"Libro con ISBN {isbn} no encontrado")


class LibroNoDisponible(ErrorBiblioteca):
    def __init__(self, titulo):
        super().__init__(f"No hay copias disponibles de '{titulo}'")


class UsuarioNoRegistrado(ErrorBiblioteca):
    def __init__(self, id_usuario):
        super().__init__(f"Usuario con ID '{id_usuario}' no está registrado")


class LimitePrestamosExcedido(ErrorBiblioteca):
    def __init__(self, id_usuario, limite):
        super().__init__(f"Usuario {id_usuario} excede límite de {limite} préstamos")


# ===================== CLASE PRINCIPAL =====================

class SistemaBiblioteca:
    def __init__(self, dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3):
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}
        self.contador_prestamos = {}
        self._next_prestamo_id = 1
        self.dias_prestamo = dias_prestamo
        self.multa_por_dia = multa_por_dia
        self.limite_prestamos = limite_prestamos

        self._cargar_catalogo_interno()

    def _cargar_catalogo_interno(self):
        libros = [
            ("9780306406157", "El Principito", "A. Saint-Exupéry", 1943, "Infantil", 3),
            ("9780140449136", "La Iliada", "Homero", 1998, "Clásicos", 2),
            ("9788491050275", "Cien Años de Soledad", "G. García Márquez", 1967, "Novela", 4),
            ("9788420471839", "Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Clásicos", 5),
            ("9789505472413", "Rayuela", "Julio Cortázar", 1963, "Novela", 3),
            ("9789588886511", "La María", "Jorge Isaacs", 1867, "Romance", 2),
            ("9788408172173", "Orgullo y Prejuicio", "Jane Austen", 1813, "Romance", 4),
            ("9788445071738", "El Hobbit", "J.R.R. Tolkien", 1937, "Fantasía", 6),
            ("9788437604947", "La Odisea", "Homero", 1992, "Clásicos", 2),
            ("9788445071684", "El Señor de los Anillos", "J.R.R. Tolkien", 1954, "Fantasía", 7)
        ]

        for isbn, titulo, autor, anio, categoria, copias in libros:
            self.catalogo[isbn] = {
                "titulo": titulo,
                "autor": autor,
                "anio": anio,
                "categoria": categoria,
                "copias_total": copias,
                "copias_disponibles": copias
            }
            self.contador_prestamos[isbn] = 0

    def registrar_usuario(self, id_usuario, nombre, email):
        if id_usuario in self.usuarios:
            raise ValueError("El ID de usuario ya está registrado.")
        self.usuarios[id_usuario] = {
            "nombre": nombre,
            "email": email,
            "prestamos_activos": [],
            "historial": []
        }

    def prestar_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)

        libro = self.catalogo[isbn]
        if libro["copias_disponibles"] <= 0:
            raise LibroNoDisponible(libro["titulo"])

        usuario = self.usuarios[id_usuario]
        if len(usuario["prestamos_activos"]) >= self.limite_prestamos:
            raise LimitePrestamosExcedido(id_usuario, self.limite_prestamos)

        pid = f"P{self._next_prestamo_id:06d}"
        self._next_prestamo_id += 1
        fecha_prestamo = datetime.now()
        fecha_vencimiento = fecha_prestamo + timedelta(days=self.dias_prestamo)

        self.prestamos[pid] = {
            "isbn": isbn,
            "id_usuario": id_usuario,
            "fecha_prestamo": fecha_prestamo,
            "fecha_vencimiento": fecha_vencimiento,
            "fecha_devolucion": None,
            "multa": 0.0
        }

        libro["copias_disponibles"] -= 1
        usuario["prestamos_activos"].append(pid)
        usuario["historial"].append(pid)
        self.contador_prestamos[isbn] += 1

        return pid

    def devolver_libro(self, id_prestamo):
        if id_prestamo not in self.prestamos:
            raise ValueError("El préstamo no existe.")

        p = self.prestamos[id_prestamo]
        if p["fecha_devolucion"]:
            raise ValueError("El libro ya fue devuelto.")

        hoy = datetime.now()
        p["fecha_devolucion"] = hoy

        dias_retraso = max(0, (hoy.date() - p["fecha_vencimiento"].date()).days)
        multa = dias_retraso * self.multa_por_dia
        p["multa"] = multa

        self.catalogo[p["isbn"]]["copias_disponibles"] += 1
        self.usuarios[p["id_usuario"]]["prestamos_activos"].remove(id_prestamo)

        return {"dias_retraso": dias_retraso, "multa": multa}

    def libros_mas_prestados(self, n=5):
        lista = [(isbn, d["titulo"], self.contador_prestamos[isbn]) for isbn, d in self.catalogo.items()]
        return sorted(lista, key=lambda x: x[2], reverse=True)[:n]

    def estadisticas_categoria(self, categoria):
        conteos = {}
        total_libros = total_copias = prestadas = 0

        for isbn, d in self.catalogo.items():
            if d["categoria"].lower() == categoria.lower():
                total_libros += 1
                total_copias += d["copias_total"]
                prestadas += d["copias_total"] - d["copias_disponibles"]
                conteos[isbn] = self.contador_prestamos[isbn]

        if conteos:
            top = max(conteos, key=conteos.get)
            popular = self.catalogo[top]["titulo"]
        else:
            popular = "Sin datos"

        tasa = (prestadas / total_copias) if total_copias else 0
        return {
            "total_libros": total_libros,
            "total_copias": total_copias,
            "copias_prestadas": prestadas,
            "tasa_prestamo": round(tasa, 2),
            "libro_mas_popular": popular
        }

def menu():
    biblioteca = SistemaBiblioteca()
    biblioteca.registrar_usuario("u001", "Ana Pérez", "ana@example.com")
    biblioteca.registrar_usuario("u002", "Carlos Ruiz", "carlos@example.com")

    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Ver catálogo")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Libros más prestados")
        print("5. Estadísticas por categoría")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nCATÁLOGO DISPONIBLE:")
            for isbn, d in biblioteca.catalogo.items():
                print(f"{d['titulo']} ({isbn}) - {d['categoria']} [{d['copias_disponibles']} disp.]")

        elif opcion == "2":
            isbn = input("ISBN del libro: ")
            usuario = input("ID del usuario: ")
            try:
                pid = biblioteca.prestar_libro(isbn, usuario)
                print(f"Libro prestado con éxito. ID de préstamo: {pid}")
            except Exception as e:
                print("Error:", e)

        elif opcion == "3":
            pid = input("ID del préstamo: ")
            try:
                info = biblioteca.devolver_libro(pid)
                print(f"Libro devuelto. Multa: ${info['multa']:.2f}")
            except Exception as e:
                print("Error:", e)

        elif opcion == "4":
            print("\nLibros más prestados:")
            for isbn, titulo, veces in biblioteca.libros_mas_prestados():
                print(f" - {titulo} ({isbn}) → {veces} préstamo(s)")

        elif opcion == "5":
            cat = input("Ingresa la categoría: ")
            print(biblioteca.estadisticas_categoria(cat))

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# ===================== EJECUCIÓN =====================

if __name__ == "__main__":
    menu()
