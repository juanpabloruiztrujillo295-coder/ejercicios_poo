#!/usr/bin/env python3
"""
EJERCICIOS PARA ESTUDIANTES - ESTRUCTURAS DE CONTROL
Completa los siguientes ejercicios mientras exploramos los conceptos confusos.
"""

def ejercicio_1():
    """
    Problema: El siguiente código debería imprimir solo los números impares,
    pero tiene un error porque modifica la lista mientras la recorre.
    Corrígelo para que funcione correctamente.
    """
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Código original con error
    print("Código original (con error):")
    print("numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
    print("for num in numeros:")
    print("    if num % 2 == 0:  # Si es par")
    print("        numeros.remove(num)")
    print("print(numeros)")
    
    print("\nResultado esperado: [1, 3, 5, 7, 9]")
    
    # Tu corrección
    print("\nTu solución:")
    # Escribe aquí tu código corregido
    numeros = [n for n in numeros if n % 2 != 0]
    
    return "¡Completa el ejercicio!"

def ejercicio_2():
    """
    Problema: Completa el código para generar una tabla de multiplicar
    del 1 al 10 usando bucles anidados.
    """
    print("Tabla de multiplicar del 1 al 10:")
    
    # Completa el código aquí
    for fila in range(1, 6):         
        for columna in range(1, 3):  
            numero = (fila - 1) * 2 + columna
            print(numero, end="  ")
    print()  
    # Usa bucles anidados para generar la tabla
    
    return "¡Completa el ejercicio!"

def ejercicio_3():
    """
    Problema: El siguiente bucle while debería imprimir los números del 1 al 5,
    pero tiene un problema que lo convierte en infinito. Corrígelo.
    """
    print("Bucle while para imprimir números del 1 al 5:")
    
    # Código original con error
    print("Código original (con error):")
    print("contador = 1")
    print("while contador <= 5:")
    print('    print(f"Número: {contador}")')
    print("    # Falta algo aquí")
    
    # Tu corrección
    print("\nTu solución:")
    # Escribe aquí tu código corregido
    
    return "¡Completa el ejercicio!"

def ejercicio_4():
    """
    Problema: Usa break y continue adecuadamente para procesar la siguiente lista
    de números: imprime cada número, pero salta los negativos y detén el proceso
    al encontrar un cero.
    """
    numeros = [5, -2, 10, 8, -3, 0, 7, 9]
    
    print(f"Lista de números: {numeros}")
    print("Resultado esperado: Imprime solo positivos y termina al encontrar 0")
    
    # Completa el código aquí
    
    return "¡Completa el ejercicio!"

def ejercicio_5():
    """
    Problema: Reescribe el siguiente código utilizando una comprensión de lista.
    """
    print("Código original:")
    print("cuadrados_pares = []")
    print("for numero in range(1, 11):")
    print("    if numero % 2 == 0:")
    print("        cuadrados_pares.append(numero ** 2)")
    print("print(cuadrados_pares)")
    
    # Versión con bucle tradicional para comparar
    cuadrados_pares = []
    for numero in range(1, 11):
        if numero % 2 == 0:
            cuadrados_pares.append(numero ** 2)
    print(f"\nResultado con bucle tradicional: {cuadrados_pares}")
    
    # Tu solución con comprensión de lista
    print("\nTu solución con comprensión de lista:")
    # Escribe aquí tu código
    
    return "¡Completa el ejercicio!"

def ejercicio_6():
    """
    Problema: Usa bucles anidados para encontrar todas las combinaciones
    posibles de dos listas. Luego implementa el mismo resultado usando
    comprensión de listas.
    """
    colores = ["rojo", "azul", "verde"]
    tamaños = ["pequeño", "mediano", "grande"]
    
    print(f"Colores: {colores}")
    print(f"Tamaños: {tamaños}")
    print("Combinaciones esperadas: [('rojo', 'pequeño'), ('rojo', 'mediano'), ...]")
    
    print("\n1. Solución con bucles anidados:")
    # Completa el código aquí
    
    print("\n2. Solución con comprensión de listas:")
    # Completa el código aquí
    
    return "¡Completa el ejercicio!"

def menu():
    """
    Muestra un menú para seleccionar qué ejercicio ejecutar.
    """
    print("\n" + "=" * 50)
    print("EJERCICIOS DE ESTRUCTURAS DE CONTROL".center(50))
    print("=" * 50)
    
    print("\nSelecciona un ejercicio:")
    print("1. Corregir iteración y modificación de lista")
    print("2. Tabla de multiplicar con bucles anidados")
    print("3. Corregir bucle while infinito")
    print("4. Uso de break y continue")
    print("5. Convertir bucle a comprensión de lista")
    print("6. Combinaciones con bucles anidados")
    print("0. Salir")
    
    try:
        opcion = int(input("\nIngresa el número del ejercicio (0-6): "))
        return opcion
    except ValueError:
        print("Entrada inválida. Ingresa un número del 0 al 6.")
        return -1

def main():
    """
    Función principal para ejecutar los ejercicios.
    """
    while True:
        opcion = menu()
        
        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_4()
        elif opcion == 5:
            ejercicio_5()
        elif opcion == 6:
            ejercicio_6()
        else:
            print("Opción inválida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
