#!/usr/bin/env python3
"""
PARCIAL 2 - EJERCICIOS (Parte 1)
Estudiante: Juan Pablo Ruiz Trujillo
Fecha: 19/10/2025
"""

# ===========================================================================
# EJERCICIO 1: EXPRESIONES ARITMÉTICAS (10 puntos)
# ===========================================================================

def calculadora_cientifica(operacion, a, b):
    # Verificar que los valores sean números
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise ValueError("Error: los valores deben ser números.")

    # Suma
    if operacion == "suma":
        resultado = a + b
    # Resta
    elif operacion == "resta":
        resultado = a - b
    # Multiplicación
    elif operacion == "multiplicacion":
        resultado = a * b
    # División (verificando que no sea entre 0)
    elif operacion == "division":
        if b == 0:
            raise ZeroDivisionError("Error: no se puede dividir entre cero.")
        resultado = a / b
    # Potencia
    elif operacion == "potencia":
        resultado = a ** b
    else:
        raise ValueError("Operación no válida.")

    return round(resultado, 2)

print("=== CALCULADORA CIENTÍFICA ===")
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("===============================")

# Pedir al usuario que elija una operación
opcion = input("Elige una operación (1-6): ")

if opcion == "1":
    operacion = "suma"
elif opcion == "2":
    operacion = "resta"
elif opcion == "3":
    operacion = "multiplicacion"
elif opcion == "4":
    operacion = "division"
elif opcion == "5":
    operacion = "potencia"
elif opcion == "6":
    operacion = "modulo"
else:
    print("Opción no válida. Intenta de nuevo.")
    exit()

# Pedir los números al usuario
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

# Intentar realizar la operación
try:
    resultado = calculadora_cientifica(operacion, a, b)
    print(f"El resultado de la {operacion} es: {resultado}")
except Exception as e:
    print("Ocurrió un error:", e)

# ===========================================================================
# EJERCICIO 2: EXPRESIONES LÓGICAS Y RELACIONALES (12 puntos)
# ===========================================================================

class ValidadorPassword:
    
    def __init__(self, min_longitud=8, requiere_mayuscula=True, 
                requiere_minuscula=True, requiere_numero=True, 
                requiere_especial=True):
        self.min_longitud = min_longitud
        self.requiere_mayuscula = requiere_mayuscula
        self.requiere_minuscula = requiere_minuscula
        self.requiere_numero = requiere_numero
        self.requiere_especial = requiere_especial

    def validar(self, password):
        errores = []

        if len(password) < self.min_longitud:
            errores.append(f"Debe tener al menos {self.min_longitud} caracteres.")
        if self.requiere_mayuscula and not any(c.isupper() for c in password):
            errores.append("Debe incluir una letra mayúscula.")
        if self.requiere_minuscula and not any(c.islower() for c in password):
            errores.append("Debe incluir una letra minúscula.")
        if self.requiere_numero and not any(c.isdigit() for c in password):
            errores.append("Debe incluir un número.")
        especiales = "!@#$%^&*()-_=+[]{};:,<.>/?"
        if self.requiere_especial and not any(c in especiales for c in password):
            errores.append("Debe incluir un carácter especial.")

        if errores:
            return (False, errores)
        else:
            return (True, [])

    def es_fuerte(self, password):
        tiene_may = any(c.isupper() for c in password)
        tiene_min = any(c.islower() for c in password)
        tiene_num = any(c.isdigit() for c in password)
        tiene_esp = any(c in "!@#$%^&*()-_=+[]{};:,<.>/?" for c in password)
        return len(password) >= 12 and tiene_may and tiene_min and tiene_num and tiene_esp

def menu():
    validador = ValidadorPassword()
    
    while True:
        print("\n=== VALIDACIÓN DE CONTRASEÑAS ===")
        print("1. Validar contraseña")
        print("2. Comprobar si es fuerte")
        print("3. Cambiar reglas")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            pwd = input("Ingresa la contraseña: ")
            valido, errores = validador.validar(pwd)
            if valido:
                print("Contraseña válida.")
            else:
                print("Errores encontrados:")
                for e in errores:
                    print(" -", e)

        elif opcion == "2":
            pwd = input("Ingresa la contraseña: ")
            if validador.es_fuerte(pwd):
                print("La contraseña es fuerte.")
            else:
                print("No es una contraseña fuerte.")

        elif opcion == "3":
            print("=== Configurar reglas ===")
            validador.min_longitud = int(input("Longitud mínima: "))
            validador.requiere_mayuscula = input("¿Requiere mayúscula? (s/n): ").lower() == "s"
            validador.requiere_minuscula = input("¿Requiere minúscula? (s/n): ").lower() == "s"
            validador.requiere_numero = input("¿Requiere número? (s/n): ").lower() == "s"
            validador.requiere_especial = input("¿Requiere especial? (s/n): ").lower() == "s"
            print("Reglas actualizadas.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

menu()

# ===========================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS (15 puntos)
# ===========================================================================

class GestorInventario:

    def __init__(self):
        self.inventario = {} 

    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        if codigo in self.inventario:
            print("Ese código ya existe.")
        else:
            self.inventario[codigo] = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
                "categoria": categoria
            }
            print("Producto agregado correctamente.")

    def actualizar_stock(self, codigo, cantidad_cambio):
        if codigo not in self.inventario:
            print("El producto no existe.")
        else:
            nuevo_stock = self.inventario[codigo]["cantidad"] + cantidad_cambio
            if nuevo_stock < 0:
                print("No se puede tener stock negativo.")
            else:
                self.inventario[codigo]["cantidad"] = nuevo_stock
                print("Stock actualizado.")

    def buscar_por_categoria(self, categoria):
        return [
            (cod, datos["nombre"], datos["precio"])
            for cod, datos in self.inventario.items()
            if datos["categoria"].lower() == categoria.lower()
        ]

    def productos_bajo_stock(self, limite=10):
        return {
            cod: datos["cantidad"]
            for cod, datos in self.inventario.items()
            if datos["cantidad"] < limite
        }

    def valor_total_inventario(self):
        return sum(datos["precio"] * datos["cantidad"]
                    for datos in self.inventario.values())

# Menú
gestor = GestorInventario()

while True:
    print("\n=== MENÚ INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Actualizar stock")
    print("3. Buscar por categoría")
    print("4. Productos con bajo stock")
    print("5. Ver valor total del inventario")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        codigo = input("Código del producto: ")
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        categoria = input("Categoría: ")
        gestor.agregar_producto(codigo, nombre, precio, cantidad, categoria)

    elif opcion == "2":
        codigo = input("Código del producto: ")
        cambio = int(input("Cantidad a sumar o restar: "))
        gestor.actualizar_stock(codigo, cambio)

    elif opcion == "3":
        cat = input("Categoría a buscar: ")
        lista = gestor.buscar_por_categoria(cat)
        if not lista:
            print("No hay productos en esa categoría.")
        else:
            print("Productos encontrados:")
            for codigo, nombre, precio in lista:
                print(f"- {nombre} (${precio})")

    elif opcion == "4":
        limite = int(input("Límite de stock: "))
        bajos = gestor.productos_bajo_stock(limite)
        if not bajos:
            print("Todo el inventario está en buen nivel.")
        else:
            print("Productos con poco stock:")
            for codigo, cantidad in bajos.items():
                print(f"- {codigo}: {cantidad} unidades")

    elif opcion == "5":
        total = gestor.valor_total_inventario()
        print(f"Valor total del inventario: ${total:.2f}")

    elif opcion == "6":
        print("Saliendo del programa..")

# ===========================================================================
# EJERCICIO 4: ESTRUCTURAS DE CONTROL (10 puntos)
# ===========================================================================

def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def dias_en_mes(mes, año):
    if mes < 1 or mes > 12:
        raise ValueError("El mes debe estar entre 1 y 12")

    meses = [31, 29 if es_bisiesto(año) else 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    return meses[mes - 1]


def generar_calendario(mes, año, dia_inicio=0):
    dias_semana = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do"]
    dias_mes = dias_en_mes(mes, año)

    calendario = " ".join(dias_semana) + "\n"
    calendario += "   " * dia_inicio 

    dias = [f"{d:2}" for d in range(1, dias_mes + 1)]

    for i, dia in enumerate(dias, start=dia_inicio):
        calendario += f"{dia} "
        if (i + 1) % 7 == 0:
            calendario += "\n"

    return calendario

# Menú

while True:
    print("\n=== MENÚ CALENDARIO ===")
    print("1. Ver si un año es bisiesto")
    print("2. Ver cuántos días tiene un mes")
    print("3. Mostrar calendario del mes")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        año = int(input("Ingresa el año: "))
        if es_bisiesto(año):
            print(f"El año {año} es bisiesto.")
        else:
            print(f"El año {año} NO es bisiesto.")

    elif opcion == "2":
        mes = int(input("Ingresa el mes (1-12): "))
        año = int(input("Ingresa el año: "))
        try:
            print(f"El mes {mes} del año {año} tiene {dias_en_mes(mes, año)} días.")
        except ValueError as e:
            print("Error:", e)

    elif opcion == "3":
        mes = int(input("Ingresa el mes (1-12): "))
        año = int(input("Ingresa el año: "))
        dia_inicio = int(input("Día de inicio (0=Lunes, 6=Domingo): "))
        print(f"\n=== Calendario de {mes}/{año} ===")
        print(generar_calendario(mes, año, dia_inicio))

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta de nuevo.")

# ===========================================================================
# EJERCICIO 5: ESTRUCTURAS DE REPETICIÓN (13 puntos)
# ===========================================================================

def analizar_ventas(ventas):
    if not ventas:
        return {"error": "No hay ventas registradas"}

    total_ventas = sum(v["cantidad"] * v["precio"] * (1 - v["descuento"]) for v in ventas)
    promedio_por_venta = total_ventas / len(ventas)
    producto_mas_vendido = max(ventas, key=lambda v: v["cantidad"])["producto"]
    venta_mayor = max(ventas, key=lambda v: v["cantidad"] * v["precio"])
    total_descuentos = sum(v["cantidad"] * v["precio"] * v["descuento"] for v in ventas)

    return {
        "total_ventas": round(total_ventas, 2),
        "promedio_por_venta": round(promedio_por_venta, 2),
        "producto_mas_vendido": producto_mas_vendido,
        "venta_mayor": venta_mayor,
        "total_descuentos": round(total_descuentos, 2)
    }

def encontrar_patrones(numeros):
    """Encuentra patrones en una secuencia de números."""
    if not numeros:
        return {"error": "Lista vacía"}

    asc, desc = 0, 0
    max_asc, max_desc = 0, 0
    repetidos = {}

    actual_asc, actual_desc = 1, 1

    for i in range(1, len(numeros)):
        if numeros[i] > numeros[i - 1]:
            actual_asc += 1
            max_asc = max(max_asc, actual_asc)
            actual_desc = 1
        elif numeros[i] < numeros[i - 1]:
            actual_desc += 1
            max_desc = max(max_desc, actual_desc)
            actual_asc = 1
        else:
            actual_asc = actual_desc = 1

    asc = sum(1 for i in range(1, len(numeros)) if numeros[i] > numeros[i - 1])
    desc = sum(1 for i in range(1, len(numeros)) if numeros[i] < numeros[i - 1])
    repetidos = {n: numeros.count(n) for n in set(numeros) if numeros.count(n) > 1}

    return {
        "secuencias_ascendentes": asc,
        "secuencias_descendentes": desc,
        "longitud_max_ascendente": max_asc,
        "longitud_max_descendente": max_desc,
        "numeros_repetidos": repetidos
    }

def simular_crecimiento(principal, tasa_anual, años, aporte_anual=0):
    resultados = []
    balance = principal

    for año in range(1, años + 1):
        balance += aporte_anual
        interes = balance * tasa_anual
        balance += interes
        resultados.append({
            "año": año,
            "balance": round(balance, 2),
            "interes_ganado": round(interes, 2)
        })
    return resultados

# Menú

while True:
    print("\n=== MENÚ DE FUNCIONES ===")
    print("1. Analizar ventas")
    print("2. Encontrar patrones en números")
    print("3. Simular crecimiento de inversión")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        ventas = [
            {"producto": "Pan", "cantidad": 10, "precio": 2.5, "descuento": 0.1},
            {"producto": "Leche", "cantidad": 5, "precio": 3.0, "descuento": 0.05},
            {"producto": "Huevos", "cantidad": 20, "precio": 0.5, "descuento": 0.0}
        ]
        print("\nResultado del análisis de ventas:")
        print(analizar_ventas(ventas))

    elif opcion == "2":
        numeros = [3, 5, 7, 6, 4, 8, 9, 9, 2, 1]
        print("\nPatrones encontrados:")
        print(encontrar_patrones(numeros))

    elif opcion == "3":
        principal = float(input("Monto inicial: "))
        tasa = float(input("Tasa anual (ej: 0.05 para 5%): "))
        años = int(input("Años: "))
        aporte = float(input("Aporte anual: "))

        print("\nSimulación de inversión:")
        for fila in simular_crecimiento(principal, tasa, años):
            print(f"Año {fila['anio']}: balance = {fila['balance']}, interés ganado = {fila['interes_ganado']}")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta de nuevo.")