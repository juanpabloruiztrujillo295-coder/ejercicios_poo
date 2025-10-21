#!/usr/bin/env python3
"""
EJERCICIOS PARA ESTUDIANTES - MANEJO DE EXCEPCIONES
Completa estos ejercicios mientras exploras los conceptos confusos de manejo de excepciones.
"""

# ===========================================================================
# Ejercicio 1: Encuentra y arregla el except desnudo
# ===========================================================================
print("\n--- EJERCICIO 1: ARREGLA EL EXCEPT DESNUDO ---")
print("Esta función tiene un except desnudo. Arréglalo para capturar excepciones específicas.")
print()

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    ARREGLA: Usa manejo de excepciones específico en lugar de except desnudo.
    """
    try:
        total = sum(numeros)
        promedio = total / len(numeros)
        return promedio
    except ZeroDivisionError:
        print("Error: la lista está vacía (división por cero).")
        return None
    except TypeError:
        print("Error: la lista contiene elementos no numéricos.")
        return None

# Prueba tu arreglo:
# print(calcular_promedio([1, 2, 3, 4, 5]))  # Debería funcionar
# print(calcular_promedio([]))  # Debería manejar lista vacía
# print(calcular_promedio([1, 2, 'a']))  # Debería manejar error de tipo

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Ejercicio 2: Añade retroalimentación al usuario
# ===========================================================================
print("\n--- EJERCICIO 2: AÑADE RETROALIMENTACIÓN ---")
print("Este código falla silenciosamente. Añade mensajes apropiados.")
print()

def guardar_datos(datos, archivo):
    """
    Guarda datos en un archivo.
    ARREGLA: Añade manejo de excepciones Y feedback al usuario.
    """
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(str(datos))
        print(f"Datos guardados correctamente en '{archivo}'.")
        return True
    except (OSError, IOError) as e:
        print(f"Error al guardar datos en '{archivo}': {e}")
        return False

# Prueba tu arreglo:
# guardar_datos({"usuario": "Ana"}, "datos.txt")  # Debería funcionar
# guardar_datos({"usuario": "Ana"}, "/ruta/invalida/datos.txt")  # Debería informar error

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Ejercicio 3: Usa else y finally correctamente
# ===========================================================================
print("\n--- EJERCICIO 3: USA ELSE Y FINALLY ---")
print("Implementa un manejo completo de archivos con else y finally.")
print()

def procesar_archivo(nombre_archivo):
    """
    Lee y procesa un archivo.
    - try: abrir y leer archivo
    - except: manejar FileNotFoundError
    - else: procesar los datos (solo si lectura exitosa)
    - finally: asegurar que el archivo se cierre
    """
    f = None
    try:
        f = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = f.read()
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
        return None
    except (OSError, IOError) as e:
        print(f"Error al leer el archivo '{nombre_archivo}': {e}")
        return None
    else:
        # Procesamiento simple: contar líneas y palabras
        lineas = contenido.splitlines()
        num_lineas = len(lineas)
        num_palabras = sum(len(linea.split()) for linea in lineas)
        print(f"Archivo '{nombre_archivo}' leído correctamente: {num_lineas} líneas, {num_palabras} palabras.")
        return {"lineas": num_lineas, "palabras": num_palabras}
    finally:
        if f:
            try:
                f.close()
            except Exception:
                pass

# Prueba tu implementación:
# procesar_archivo("existente.txt")
# procesar_archivo("faltante.txt")

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Ejercicio 4: Lanza excepciones apropiadas
# ===========================================================================
print("\n--- EJERCICIO 4: LANZA EXCEPCIONES ---")
print("Implementa validación con excepciones específicas.")
print()

def crear_usuario(nombre_usuario, edad, email):
    """
    Crea un nuevo usuario con validación.
    - nombre_usuario tiene menos de 3 caracteres -> ValueError
    - edad no es un entero -> TypeError
    - edad es negativa o mayor a 150 -> ValueError
    - email no contiene '@' -> ValueError
    """
    if not isinstance(nombre_usuario, str) or len(nombre_usuario) < 3:
        raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0 or edad > 150:
        raise ValueError("Edad inválida. Debe estar entre 0 y 150.")
    if not isinstance(email, str) or '@' not in email:
        raise ValueError("Email inválido. Debe contener '@'.")
    # Si todo bien, devolver un dict con datos del usuario
    usuario = {"nombre": nombre_usuario, "edad": edad, "email": email}
    print(f"Usuario creado: {usuario}")
    return usuario

# Prueba tu implementación:
# crear_usuario("Ana", 25, "ana@example.com")  # Debería funcionar
# crear_usuario("Ab", 25, "ana@example.com")  # Debería lanzar ValueError
# crear_usuario("Ana", "25", "ana@example.com")  # Debería lanzar TypeError
# crear_usuario("Ana", -5, "ana@example.com")  # Debería lanzar ValueError
# crear_usuario("Ana", 25, "anaexample.com")  # Debería lanzar ValueError

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Ejercicio 5: Crea excepciones personalizadas
# ===========================================================================
print("\n--- EJERCICIO 5: EXCEPCIONES PERSONALIZADAS ---")
print("Crea excepciones personalizadas para un sistema bancario.")
print()

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        self.saldo = saldo
        self.monto = monto
        super().__init__(f"Saldo insuficiente: necesitas ${monto}, tienes ${saldo}")

class MontoInvalidoError(Exception):
    pass

def retirar(saldo, monto):
    """
    Retira dinero de una cuenta.
    - Lanza MontoInvalidoError si monto <= 0
    - Lanza SaldoInsuficienteError si monto > saldo
    - Retorna nuevo saldo si exitoso
    """
    if monto <= 0:
        raise MontoInvalidoError("El monto a retirar debe ser mayor que cero.")
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    nuevo_saldo = saldo - monto
    print(f"Retiro exitoso: nuevo saldo = ${nuevo_saldo}")
    return nuevo_saldo

# Prueba tu implementación:
# print(retirar(100, 50))  # Debería funcionar
# retirar(100, 150)  # Debería lanzar SaldoInsuficienteError
# retirar(100, -10)  # Debería lanzar MontoInvalidoError

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Ejercicio 6: Maneja excepciones en bucles
# ===========================================================================
print("\n--- EJERCICIO 6: EXCEPCIONES EN BUCLES ---")
print("Procesa una lista con manejo de errores.")
print()

def procesar_lista_numeros(lista_strings):
    """
    Convierte strings a números y los duplica.
    - Intenta convertir cada elemento a int
    - Si falla, registra el error pero continúa con los demás
    - Retorna tupla (resultados_exitosos, lista_errores)
    """
    resultados = []
    errores = []
    for item in lista_strings:
        try:
            n = int(item)
            resultados.append(n * 2)
        except Exception as e:
            errores.append((item, str(e)))
    return resultados, errores

# Prueba tu implementación:
# resultados, errores = procesar_lista_numeros(["1", "2", "abc", "4", "xyz"])
# print(f"Exitosos: {resultados}")  # [2, 4, 8]
# print(f"Errores: {errores}")  # [('abc', error), ('xyz', error)]

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Ejercicio 7: Re-lanza excepciones apropiadamente
# ===========================================================================
print("\n--- EJERCICIO 7: RE-LANZA EXCEPCIONES ---")
print("Registra errores pero permite que el llamador los maneje.")
print()

def operacion_critica(valor):
    """
    Realiza operación crítica con logging.
    - Intenta procesar valor
    - Si falla, registra el error (print)
    - Re-lanza la excepción para que el llamador pueda manejarla
    """
    try:
        resultado = 100 / int(valor)
        return resultado
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error en operacion_critica con valor={valor}: {e}")
        raise

# Prueba tu implementación:
# print(operacion_critica("10"))  # Debería funcionar
# try:
#     operacion_critica("0")  # Debería registrar y re-lanzar
# except ZeroDivisionError:
#     print("Llamador: Manejo el error")

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Ejercicio 8: Excepción con múltiples except
# ===========================================================================
print("\n--- EJERCICIO 8: MÚLTIPLES EXCEPT ---")
print("Maneja diferentes tipos de errores de manera diferente.")
print()

def calculadora_segura(operacion, a, b):
    """
    Realiza operaciones matemáticas con manejo de errores.
    - ZeroDivisionError: retorna mensaje específico
    - TypeError: retorna mensaje específico
    - ValueError: retorna mensaje específico (operación inválida)
    """
    try:
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        elif operacion == "multiplicacion":
            return a * b
        elif operacion == "division":
            return a / b
        else:
            raise ValueError("Operación no válida.")
    except ZeroDivisionError:
        return "Error: División por cero."
    except TypeError:
        return "Error: Tipos de datos inválidos para la operación."
    except ValueError as e:
        return f"Error: {e}"

# Prueba tu implementación:
# print(calculadora_segura("suma", 10, 5))  # 15
# print(calculadora_segura("division", 10, 0))  # Maneja división por cero
# print(calculadora_segura("suma", 10, "5"))  # Maneja error de tipo
# print(calculadora_segura("invalida", 10, 5))  # Maneja operación inválida

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Ejercicio 9: Contexto de excepción
# ===========================================================================
print("\n--- EJERCICIO 9: CONTEXTO DE EXCEPCIÓN ---")
print("Preserva el contexto al lanzar nuevas excepciones.")
print()

def parsear_configuracion(json_string):
    """
    Parsea configuración JSON.
    - Intenta parsear JSON
    - Si falla, lanza ValueError con 'from' para preservar el error original
    """
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError("JSON inválido") from e

# Prueba tu implementación:
# print(parsear_configuracion('{"nombre": "Ana"}'))  # Debería funcionar
# try:
#     parsear_configuracion('json invalido')
# except ValueError as e:
#     print(f"Error: {e}")
#     print(f"Causado por: {e.__cause__}")

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Ejercicio 10: Proyecto completo
# ===========================================================================
print("\n--- EJERCICIO 10: PROYECTO COMPLETO ---")
print("Crea un sistema de gestión de inventario con manejo completo de excepciones.")
print()

# Excepciones personalizadas
class ErrorInventario(Exception):
    pass

class ProductoNoEncontrado(ErrorInventario):
    def __init__(self, codigo):
        super().__init__(f"Producto con código '{codigo}' no encontrado.")

class StockInsuficiente(ErrorInventario):
    def __init__(self, codigo, solicitado, disponible):
        super().__init__(f"Stock insuficiente para '{codigo}': solicitado {solicitado}, disponible {disponible}.")

class Inventario:
    """Sistema de inventario con manejo completo de excepciones."""
    
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, codigo, nombre, cantidad):
        """
        Añade producto al inventario.
        - Validar que cantidad sea positiva (ValueError)
        - Validar que codigo no exista ya (KeyError)
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if codigo in self.productos:
            raise KeyError(f"El código '{codigo}' ya existe.")
        self.productos[codigo] = {"nombre": nombre, "cantidad": int(cantidad)}
        print(f"Producto agregado: {codigo} - {nombre} ({cantidad})")
    
    def retirar_stock(self, codigo, cantidad):
        """
        Retira cantidad de un producto.
        - Verificar que producto existe (ProductoNoEncontrado)
        - Verificar que hay suficiente stock (StockInsuficiente)
        """
        if codigo not in self.productos:
            raise ProductoNoEncontrado(codigo)
        disponible = self.productos[codigo]["cantidad"]
        if cantidad > disponible:
            raise StockInsuficiente(codigo, cantidad, disponible)
        self.productos[codigo]["cantidad"] -= cantidad
        print(f"Retirado {cantidad} de {codigo}. Quedan {self.productos[codigo]['cantidad']}")
        return self.productos[codigo]["cantidad"]
    
    def obtener_producto(self, codigo):
        """
        Obtiene información de un producto.
        - Lanzar ProductoNoEncontrado si no existe
        """
        if codigo not in self.productos:
            raise ProductoNoEncontrado(codigo)
        return {"codigo": codigo, **self.productos[codigo]}

# Prueba tu implementación:
# inventario = Inventario()
# inventario.agregar_producto("001", "Laptop", 10)
# print(inventario.obtener_producto("001"))
# inventario.retirar_stock("001", 5)
# # Prueba casos de error...

print("¿Completado? [Sí/No]: _____")


# ===========================================================================
# Reflexión Final
# ===========================================================================
print("\n" + "=" * 70)
print(" REFLEXIÓN")
print("=" * 70 + "\n")

print("Después de completar estos ejercicios, reflexiona:")
print()
print("1. ¿Qué tipos de excepciones usaste más frecuentemente?")
print("2. ¿Cuándo decidiste crear excepciones personalizadas?")
print("3. ¿Qué patrón de manejo de excepciones te pareció más útil?")
print("4. ¿Cómo ayuda el manejo de excepciones a la experiencia del usuario?")
print("5. ¿Qué errores comunes evitaste con el manejo apropiado?")
print()
print("Discute tus respuestas con un compañero o con el profesor.")
print()

print("=" * 70)
print(" ¡EJERCICIOS COMPLETADOS!")
print("=" * 70)


# ===========================
# EJECUCIÓN DE PRUEBAS UNO DETRÁS DEL OTRO
# ===========================
if __name__ == "__main__":
    print("\n\n" + "="*70)
    print("EJECUCIÓN AUTOMÁTICA DE EJEMPLOS (uno detrás del otro)")
    print("="*70)

    # Ejercicio 1
    print("\n[E1] calcular_promedio:")
    print(" - promedio [1,2,3,4,5]:", calcular_promedio([1,2,3,4,5]))
    print(" - promedio []:", calcular_promedio([]))
    print(" - promedio [1,2,'a']:", calcular_promedio([1,2,'a']))

    # Ejercicio 2
    print("\n[E2] guardar_datos:")
    guardar_datos({"usuario": "Ana"}, "datos_prueba.txt")
    # intentar guardar en ruta inválida (solo se simula nombre inválido en algunos sistemas)
    guardar_datos({"usuario": "Ana"}, "/ruta/invalida/datos.txt")

    # Ejercicio 3
    print("\n[E3] procesar_archivo:")
    # crear archivo de prueba y procesarlo
    try:
        with open("archivo_existente.txt", "w", encoding='utf-8') as f:
            f.write("Linea1\nLinea2 palabra\nLinea3\n")
    except Exception:
        pass
    procesar_archivo("archivo_existente.txt")
    procesar_archivo("archivo_que_no_existe.txt")

    # Ejercicio 4
    print("\n[E4] crear_usuario:")
    try:
        crear_usuario("Ana", 25, "ana@example.com")
    except Exception as e:
        print("Error:", e)
    try:
        crear_usuario("Ab", 25, "ana@example.com")
    except Exception as e:
        print("Error esperado:", e)
    try:
        crear_usuario("Ana", "25", "ana@example.com")
    except Exception as e:
        print("Error esperado:", e)
    try:
        crear_usuario("Ana", -5, "ana@example.com")
    except Exception as e:
        print("Error esperado:", e)
    try:
        crear_usuario("Ana", 25, "anaexample.com")
    except Exception as e:
        print("Error esperado:", e)

    # Ejercicio 5
    print("\n[E5] retirar:")
    try:
        print(" - Nuevo saldo:", retirar(100, 50))
    except Exception as e:
        print("Error:", e)
    try:
        retirar(100, 150)
    except Exception as e:
        print("Error esperado:", e)
    try:
        retirar(100, -10)
    except Exception as e:
        print("Error esperado:", e)

    # Ejercicio 6
    print("\n[E6] procesar_lista_numeros:")
    resultados, errores = procesar_lista_numeros(["1", "2", "abc", "4", "xyz"])
    print(" - Resultados:", resultados)
    print(" - Errores:", errores)

    # Ejercicio 7
    print("\n[E7] operacion_critica:")
    try:
        print(" - 100/10 =", operacion_critica("10"))
    except Exception as e:
        print("Error:", e)
    try:
        operacion_critica("0")
    except Exception as e:
        print("Error re-lanzado y capturado por el llamador:", e)

    # Ejercicio 8
    print("\n[E8] calculadora_segura:")
    print(" - suma 10+5:", calculadora_segura("suma", 10, 5))
    print(" - division 10/0:", calculadora_segura("division", 10, 0))
    print(" - suma 10 + '5':", calculadora_segura("suma", 10, "5"))
    print(" - operacion invalida:", calculadora_segura("invalida", 10, 5))

    # Ejercicio 9
    print("\n[E9] parsear_configuracion:")
    try:
        print(" - correcto:", parsear_configuracion('{"nombre": "Ana"}'))
    except Exception as e:
        print("Error:", e)
    try:
        parsear_configuracion('json invalido')
    except Exception as e:
        print(" - Error esperado:", e)
        print("   Causa:", repr(e.__cause__))

    # Ejercicio 10
    print("\n[E10] Inventario:")
    inv = Inventario()
    try:
        inv.agregar_producto("001", "Laptop", 10)
        print(" - obtener 001:", inv.obtener_producto("001"))
        inv.retirar_stock("001", 5)
        print(" - después retiro:", inv.obtener_producto("001"))
    except Exception as e:
        print("Error:", e)
    # pruebas de error
    try:
        inv.retirar_stock("001", 10)
    except Exception as e:
        print("Error esperado:", e)
    try:
        inv.obtener_producto("999")
    except Exception as e:
        print("Error esperado:", e)

    print("\nEJECUCIÓN COMPLETA.")
