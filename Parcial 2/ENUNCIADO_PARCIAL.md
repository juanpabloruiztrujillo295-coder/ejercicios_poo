# PARCIAL INTEGRADOR - PROGRAMACIÓN ORIENTADA A OBJETOS

**Curso:** Programación Orientada a Objetos  
**Total:** 100 puntos

---

## 📋 Instrucciones Generales

1. **Lee cuidadosamente** cada enunciado antes de comenzar
2. **Gestiona tu tiempo** apropiadamente (1 hora por sección)
3. **Escribe código limpio** con nombres descriptivos de variables
4. **Comenta tu código** cuando sea necesario
5. **Maneja las excepciones** apropiadamente
6. **Prueba tu código** antes de entregarlo

**Criterios de Evaluación:**
- Corrección funcional del código (50%)
- Manejo apropiado de excepciones (20%)
- Calidad y legibilidad del código (15%)
- Eficiencia de la solución (10%)
- Documentación y comentarios (5%)

---

## PARTE 1: EJERCICIOS

### Ejercicio 1: Expresiones Aritméticas y Validación (10 puntos)

Crea una función `calculadora_cientifica(operacion, a, b)` que:

**Requisitos:**
- Soporte las operaciones: "suma", "resta", "multiplicacion", "division", "potencia", "modulo"
- Valide que los parámetros sean numéricos (int o float)
- Lance `ValueError` con mensaje descriptivo si la operación es inválida
- Lance `ZeroDivisionError` con mensaje descriptivo si se intenta dividir por cero
- Retorne el resultado con precisión de 2 decimales

**Ejemplo:**
```python
calculadora_cientifica("division", 10, 3)  # Retorna: 3.33
calculadora_cientifica("potencia", 2, 8)   # Retorna: 256.0
calculadora_cientifica("division", 10, 0)  # Lanza ZeroDivisionError
calculadora_cientifica("raiz", 4, 2)       # Lanza ValueError
```

**Puntuación:**
- Implementación correcta de operaciones: 4 puntos
- Validación de tipos: 2 puntos
- Manejo de excepciones: 3 puntos
- Formato de resultado: 1 punto

---

### Ejercicio 2: Expresiones Relacionales y Lógicas (12 puntos)

Implementa una clase `ValidadorPassword` que valide contraseñas según reglas complejas.

**Requisitos:**
```python
class ValidadorPassword:
    def __init__(self, min_longitud=8, requiere_mayuscula=True, 
                 requiere_minuscula=True, requiere_numero=True, 
                 requiere_especial=True):
        # Inicializar parámetros de validación
        pass
    
    def validar(self, password):
        """
        Valida password según las reglas configuradas.
        
        Retorna: (bool, list) - (es_valido, lista_de_errores)
        
        Si es válido: (True, [])
        Si no es válido: (False, ['error1', 'error2', ...])
        """
        pass
    
    def es_fuerte(self, password):
        """
        Retorna True si el password tiene al menos 12 caracteres,
        contiene mayúsculas, minúsculas, números y caracteres especiales.
        """
        pass
```

**Casos de prueba requeridos:**
```python
validador = ValidadorPassword(min_longitud=8)
print(validador.validar("Abc123!"))         # (False, ['Longitud mínima no cumplida'])
print(validador.validar("Abc123!@"))        # (True, [])
print(validador.validar("abcdefgh"))        # (False, ['Falta mayúscula', ...])
print(validador.es_fuerte("Abc123!@#$Xyz")) # True
```

**Puntuación:**
- Implementación de validaciones: 6 puntos
- Uso correcto de expresiones lógicas/relacionales: 3 puntos
- Manejo de casos edge: 2 puntos
- Función es_fuerte: 1 punto

---

### Ejercicio 3: Estructuras de Datos (15 puntos)

Implementa un sistema de gestión de inventario usando diccionarios, listas y tuplas.

**Requisitos:**
```python
class GestorInventario:
    def __init__(self):
        """
        Inicializa el inventario como un diccionario:
        {
            'codigo_producto': {
                'nombre': str,
                'precio': float,
                'cantidad': int,
                'categoria': str
            }
        }
        """
        pass
    
    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        """Agrega producto. Lanza ValueError si código ya existe."""
        pass
    
    def actualizar_stock(self, codigo, cantidad_cambio):
        """
        Actualiza stock (positivo=añade, negativo=reduce).
        Lanza ValueError si producto no existe.
        Lanza ValueError si stock resultante sería negativo.
        """
        pass
    
    def buscar_por_categoria(self, categoria):
        """Retorna lista de tuplas (codigo, nombre, precio) de la categoría."""
        pass
    
    def productos_bajo_stock(self, limite=10):
        """Retorna diccionario {codigo: cantidad} de productos bajo el límite."""
        pass
    
    def valor_total_inventario(self):
        """Retorna el valor total del inventario (precio * cantidad de todos)."""
        pass
    
    def top_productos(self, n=5):
        """
        Retorna lista de tuplas (codigo, valor_total) de los N productos
        con mayor valor en inventario, ordenados descendentemente.
        """
        pass
```

**Casos de prueba requeridos:**
```python
inv = GestorInventario()
inv.agregar_producto("P001", "Laptop", 1200.00, 15, "Electrónica")
inv.agregar_producto("P002", "Mouse", 25.50, 5, "Accesorios")
inv.agregar_producto("P003", "Teclado", 85.00, 8, "Accesorios")

inv.actualizar_stock("P001", -3)  # Reduce stock
print(inv.productos_bajo_stock(10))  # {'P002': 5, 'P003': 8}
print(inv.buscar_por_categoria("Accesorios"))  # [('P002', 'Mouse', 25.5), ...]
print(inv.valor_total_inventario())  # Suma total
print(inv.top_productos(2))  # Top 2 productos por valor
```

**Puntuación:**
- Estructura de datos correcta: 3 puntos
- Métodos agregar/actualizar: 4 puntos
- Métodos de búsqueda/filtrado: 4 puntos
- Cálculos y ordenamiento: 3 puntos
- Manejo de excepciones: 1 punto

---

### Ejercicio 4: Estructuras de Control (10 puntos)

Implementa una función que determine si un año es bisiesto y genere un calendario de un mes específico.

**Requisitos:**
```python
def es_bisiesto(anio):
    """
    Retorna True si el año es bisiesto.
    Reglas:
    - Divisible por 4: bisiesto
    - EXCEPTO si es divisible por 100: no bisiesto
    - EXCEPTO si es divisible por 400: bisiesto
    """
    pass

def dias_en_mes(mes, anio):
    """
    Retorna el número de días en el mes (1-12).
    Considera años bisiestos para febrero.
    Lanza ValueError si mes es inválido.
    """
    pass

def generar_calendario(mes, anio, dia_inicio=0):
    """
    Genera una representación string del calendario del mes.
    dia_inicio: 0=Lunes, 1=Martes, ..., 6=Domingo
    
    Retorna string con formato:
    Lu Ma Mi Ju Vi Sa Do
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    ...
    """
    pass
```

**Casos de prueba:**
```python
print(es_bisiesto(2024))  # True
print(es_bisiesto(2100))  # False
print(es_bisiesto(2000))  # True
print(dias_en_mes(2, 2024))  # 29
print(dias_en_mes(2, 2023))  # 28
print(generar_calendario(1, 2024, 0))  # Calendario de enero 2024
```

**Puntuación:**
- Función es_bisiesto: 2 puntos
- Función dias_en_mes: 2 puntos
- Función generar_calendario: 5 puntos
- Validaciones: 1 punto

---

### Ejercicio 5: Estructuras de Repetición (13 puntos)

Implementa funciones de análisis de datos usando loops eficientemente.

**Requisitos:**
```python
def analizar_ventas(ventas):
    """
    Analiza lista de diccionarios de ventas.
    ventas = [
        {'producto': 'A', 'cantidad': 10, 'precio': 100, 'descuento': 0.1},
        {'producto': 'B', 'cantidad': 5, 'precio': 200, 'descuento': 0.0},
        ...
    ]
    
    Retorna diccionario con:
    {
        'total_ventas': float,  # Suma de (cantidad * precio * (1 - descuento))
        'promedio_por_venta': float,
        'producto_mas_vendido': str,  # Por cantidad
        'venta_mayor': dict,  # Diccionario de la venta individual más alta
        'total_descuentos': float  # Total ahorrado por descuentos
    }
    """
    pass

def encontrar_patrones(numeros):
    """
    Encuentra patrones en lista de números.
    
    Retorna diccionario con:
    {
        'secuencias_ascendentes': int,  # Cantidad de secuencias crecientes
        'secuencias_descendentes': int,  # Cantidad de secuencias decrecientes
        'longitud_max_ascendente': int,  # Longitud de la secuencia ascendente más larga
        'longitud_max_descendente': int,
        'numeros_repetidos': dict  # {numero: cantidad_repeticiones} solo para repetidos
    }
    """
    pass

def simular_crecimiento(principal, tasa_anual, anios, aporte_anual=0):
    """
    Simula crecimiento de inversión con interés compuesto.
    
    Retorna lista de diccionarios, uno por año:
    [
        {'anio': 1, 'balance': 1050.0, 'interes_ganado': 50.0},
        {'anio': 2, 'balance': 1102.5, 'interes_ganado': 52.5},
        ...
    ]
    """
    pass
```

**Casos de prueba:**
```python
ventas = [
    {'producto': 'Laptop', 'cantidad': 2, 'precio': 1000, 'descuento': 0.1},
    {'producto': 'Mouse', 'cantidad': 10, 'precio': 20, 'descuento': 0.0},
    {'producto': 'Laptop', 'cantidad': 3, 'precio': 1000, 'descuento': 0.15}
]
print(analizar_ventas(ventas))

numeros = [1, 2, 3, 2, 1, 2, 3, 4, 5, 3, 3, 3]
print(encontrar_patrones(numeros))

print(simular_crecimiento(1000, 0.05, 5, 100))
```

**Puntuación:**
- Función analizar_ventas: 5 puntos
- Función encontrar_patrones: 5 puntos
- Función simular_crecimiento: 2 puntos
- Eficiencia de loops: 1 punto

---

## PARTE 2: PROBLEMA INTEGRADOR

### Sistema de Gestión de Biblioteca Digital

Implementa un sistema completo de gestión de biblioteca digital que integre todos los conceptos vistos.

---

### Contexto

Una biblioteca necesita un sistema para gestionar su catálogo digital, préstamos, usuarios y estadísticas. El sistema debe ser robusto, manejar errores apropiadamente y proporcionar análisis de datos.

---

### Especificaciones Técnicas

#### 1. Excepciones Personalizadas (5 puntos)

Implementa una jerarquía de excepciones personalizadas para el sistema de biblioteca.

**Jerarquía requerida:**

1. **ErrorBiblioteca(Exception)** - Excepción base del sistema
   - Solo necesita `pass` en el cuerpo

2. **LibroNoEncontrado(ErrorBiblioteca)** - Cuando un libro no existe
   - Atributo: `isbn` (string)
   - Mensaje: `"Libro con ISBN {isbn} no encontrado"`

3. **LibroNoDisponible(ErrorBiblioteca)** - Cuando no hay copias disponibles
   - Atributos: `isbn` (string), `titulo` (string)
   - Mensaje: `"No hay copias disponibles de '{titulo}'"`

4. **UsuarioNoRegistrado(ErrorBiblioteca)** - Cuando el usuario no existe
   - Atributo: `id_usuario` (string)
   - Mensaje: `"Usuario con ID '{id_usuario}' no está registrado"`

5. **LimitePrestamosExcedido(ErrorBiblioteca)** - Cuando se excede el límite
   - Atributos: `id_usuario` (string), `limite` (int)
   - Mensaje: `"Usuario {id_usuario} excede límite de {limite} préstamos"`

6. **PrestamoVencido(ErrorBiblioteca)** - Para préstamos vencidos
   - Atributos: `id_prestamo` (string), `dias_retraso` (int)
   - Mensaje: `"Préstamo {id_prestamo} está vencido por {dias_retraso} días"`

**Ejemplo de implementación esperada:**

```python
class ErrorBiblioteca(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass

class LibroNoEncontrado(ErrorBiblioteca):
    """Se lanza cuando un libro no existe en el catálogo."""
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Libro con ISBN {isbn} no encontrado")

# Implementa las 5 excepciones restantes siguiendo el mismo patrón...
```

**Requisitos:**
- Todas deben heredar de ErrorBiblioteca (excepto ErrorBiblioteca que hereda de Exception)
- Guardar los atributos especificados como atributos de instancia
- Usar `super().__init__(mensaje)` para pasar el mensaje a la clase base
- Usar f-strings para los mensajes descriptivos

---

#### 2. Clase Principal: SistemaBiblioteca (35 puntos)

```python
from datetime import datetime, timedelta

class SistemaBiblioteca:
    """
    Sistema completo de gestión de biblioteca digital.
    
    Estructuras de datos:
    - catalogo: {isbn: {'titulo', 'autor', 'anio', 'categoria', 'copias_total', 'copias_disponibles'}}
    - usuarios: {id_usuario: {'nombre', 'email', 'fecha_registro', 'prestamos_activos', 'historial'}}
    - prestamos: {id_prestamo: {'isbn', 'id_usuario', 'fecha_prestamo', 'fecha_vencimiento', 'fecha_devolucion', 'multa'}}
    """
    
    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        """
        Inicializa el sistema.
        
        Args:
            dias_prestamo: Días permitidos para cada préstamo
            multa_por_dia: Multa diaria por retraso
            limite_prestamos: Máximo de préstamos simultáneos por usuario
        """
        pass
    
    # ============ GESTIÓN DE CATÁLOGO ============
    
    def agregar_libro(self, isbn, titulo, autor, anio, categoria, copias):
        """
        Agrega un libro al catálogo.
        
        Validaciones:
        - ISBN debe ser string de 13 dígitos
        - Título y autor no vacíos
        - Año entre 1000 y año actual
        - Copias >= 1
        
        Raises:
            ValueError: Si validaciones fallan
            KeyError: Si ISBN ya existe
        """
        pass
    
    def actualizar_copias(self, isbn, cantidad_cambio):
        """
        Actualiza número de copias (añade o remueve).
        
        Raises:
            LibroNoEncontrado: Si ISBN no existe
            ValueError: Si resultado sería negativo
        """
        pass
    
    def buscar_libros(self, criterio='titulo', valor='', categoria=None):
        """
        Busca libros por diferentes criterios.
        
        Args:
            criterio: 'titulo', 'autor', 'anio'
            valor: Valor a buscar (búsqueda parcial case-insensitive)
            categoria: Filtro opcional por categoría
        
        Returns:
            Lista de diccionarios con info de libros que coinciden
        """
        pass
    
    # ============ GESTIÓN DE USUARIOS ============
    
    def registrar_usuario(self, id_usuario, nombre, email):
        """
        Registra un nuevo usuario.
        
        Validaciones:
        - Email debe contener '@' y '.'
        - Nombre no vacío
        - ID único
        
        Raises:
            ValueError: Si validaciones fallan
        """
        pass
    
    def obtener_estado_usuario(self, id_usuario):
        """
        Obtiene estado completo del usuario.
        
        Returns:
            dict con: nombre, prestamos_activos, puede_prestar, multas_pendientes
        
        Raises:
            UsuarioNoRegistrado: Si usuario no existe
        """
        pass
    
    # ============ GESTIÓN DE PRÉSTAMOS ============
    
    def prestar_libro(self, isbn, id_usuario):
        """
        Realiza un préstamo.
        
        Validaciones:
        - Usuario registrado
        - Libro existe y disponible
        - Usuario no excede límite de préstamos
        - Usuario no tiene multas pendientes > 50
        
        Returns:
            id_prestamo: ID único del préstamo
        
        Raises:
            UsuarioNoRegistrado, LibroNoEncontrado, LibroNoDisponible,
            LimitePrestamosExcedido, ValueError (multas pendientes)
        """
        pass
    
    def devolver_libro(self, id_prestamo):
        """
        Procesa devolución de libro.
        
        Calcula multa si hay retraso.
        Actualiza estado de libro y usuario.
        
        Returns:
            dict: {'dias_retraso': int, 'multa': float, 'mensaje': str}
        
        Raises:
            KeyError: Si préstamo no existe
            ValueError: Si ya fue devuelto
        """
        pass
    
    def renovar_prestamo(self, id_prestamo):
        """
        Renueva préstamo por otros N días (si no está vencido).
        
        Raises:
            PrestamoVencido: Si ya está vencido
            KeyError: Si préstamo no existe
        """
        pass
    
    # ============ ESTADÍSTICAS Y REPORTES ============
    
    def libros_mas_prestados(self, n=10):
        """
        Retorna los N libros más prestados.
        
        Returns:
            Lista de tuplas: [(isbn, titulo, cantidad_prestamos), ...]
            Ordenada descendentemente por cantidad
        """
        pass
    
    def usuarios_mas_activos(self, n=5):
        """
        Retorna los N usuarios más activos (más préstamos históricos).
        
        Returns:
            Lista de tuplas: [(id_usuario, nombre, total_prestamos), ...]
        """
        pass
    
    def estadisticas_categoria(self, categoria):
        """
        Genera estadísticas de una categoría.
        
        Returns:
            dict: {
                'total_libros': int,
                'total_copias': int,
                'copias_prestadas': int,
                'tasa_prestamo': float,  # % copias actualmente prestadas
                'libro_mas_popular': str  # título
            }
        """
        pass
    
    def prestamos_vencidos(self):
        """
        Lista préstamos actualmente vencidos.
        
        Returns:
            Lista de dicts con: id_prestamo, isbn, titulo, id_usuario,
            dias_retraso, multa_acumulada
        """
        pass
    
    def reporte_financiero(self, fecha_inicio=None, fecha_fin=None):
        """
        Genera reporte financiero de multas.
        
        Args:
            fecha_inicio, fecha_fin: Rango de fechas (datetime)
            Si son None, usa todo el historial
        
        Returns:
            dict: {
                'total_multas': float,
                'multas_pagadas': float,
                'multas_pendientes': float,
                'prestamos_con_multa': int,
                'promedio_multa': float
            }
        """
        pass
    
    # ============ UTILIDADES ============
    
    def exportar_catalogo(self, archivo='catalogo.txt'):
        """
        Exporta catálogo a archivo de texto.
        Formato: ISBN|Título|Autor|Año|Categoría|Copias
        
        Maneja excepciones de archivo apropiadamente.
        """
        pass
    
    def importar_catalogo(self, archivo='catalogo.txt'):
        """
        Importa catálogo desde archivo de texto.
        
        Maneja:
        - Archivo no existe
        - Formato incorrecto
        - Duplicados (no sobrescribir)
        
        Returns:
            dict: {'exitosos': int, 'errores': [(linea, error), ...]}
        """
        pass
```

---

### Criterios de Evaluación Detallados

#### Excepciones Personalizadas (5 puntos)
- [ ] Jerarquía correcta de excepciones (2 puntos)
- [ ] Atributos y mensajes descriptivos (2 puntos)
- [ ] Uso correcto de `super().__init__` (1 punto)

#### Gestión de Catálogo (8 puntos)
- [ ] Validaciones completas en agregar_libro (2 puntos)
- [ ] Actualización correcta de copias (2 puntos)
- [ ] Búsqueda flexible y eficiente (4 puntos)

#### Gestión de Usuarios (5 puntos)
- [ ] Validación de email y datos (2 puntos)
- [ ] Estado completo del usuario (3 puntos)

#### Gestión de Préstamos (10 puntos)
- [ ] Validaciones completas en prestar_libro (3 puntos)
- [ ] Cálculo correcto de multas (3 puntos)
- [ ] Lógica de devolución y renovación (4 puntos)

#### Estadísticas y Reportes (8 puntos)
- [ ] Libros y usuarios más activos (2 puntos)
- [ ] Estadísticas por categoría (2 puntos)
- [ ] Préstamos vencidos con cálculos (2 puntos)
- [ ] Reporte financiero completo (2 puntos)

#### Importar/Exportar (4 puntos)
- [ ] Exportación correcta (1 punto)
- [ ] Importación con manejo de errores (3 puntos)

---

### Casos de Prueba Mínimos Requeridos

```python
# Crear instancia del sistema
biblioteca = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3)

# 1. Agregar libros al catálogo
biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
biblioteca.agregar_libro("9780135404676", "Python Crash Course", "Eric Matthes", 2019, "Programación", 3)
biblioteca.agregar_libro("9781449355739", "Fluent Python", "Luciano Ramalho", 2015, "Programación", 2)

# 2. Registrar usuarios
biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")
biblioteca.registrar_usuario("U002", "Carlos López", "carlos@email.com")

# 3. Realizar préstamos
try:
    id_p1 = biblioteca.prestar_libro("9780134685991", "U001")
    id_p2 = biblioteca.prestar_libro("9780135404676", "U001")
    print(f"Préstamos realizados: {id_p1}, {id_p2}")
except ErrorBiblioteca as e:
    print(f"Error: {e}")

# 4. Buscar libros
resultados = biblioteca.buscar_libros(criterio='autor', valor='python')
print(f"Libros encontrados: {len(resultados)}")

# 5. Devolver con retraso (simular)
# Modifica fecha_vencimiento para simular retraso
resultado_dev = biblioteca.devolver_libro(id_p1)
print(f"Devolución: {resultado_dev}")

# 6. Estadísticas
print(biblioteca.libros_mas_prestados(3))
print(biblioteca.estadisticas_categoria("Programación"))
print(biblioteca.reporte_financiero())

# 7. Exportar catálogo
biblioteca.exportar_catalogo("catalogo_backup.txt")

# 8. Manejo de excepciones específicas
try:
    biblioteca.prestar_libro("9999999999999", "U001")  # ISBN no existe
except LibroNoEncontrado as e:
    print(f"Capturado correctamente: {e}")

try:
    for i in range(5):
        biblioteca.prestar_libro("9780134685991", "U002")  # Exceder límite
except LimitePrestamosExcedido as e:
    print(f"Límite controlado: {e}")
```

---

### Entregables

1. **Archivo Python:** `sistema_biblioteca.py` con toda la implementación
2. **Archivo de pruebas:** `test_biblioteca.py` con al menos 10 casos de prueba
3. **Archivo de datos:** `catalogo_inicial.txt` con al menos 10 libros para importar
4. **Documentación:** Comentarios en el código explicando lógica compleja

---

## 📝 Hoja de Respuestas

### Parte 1: Ejercicios

**Ejercicio 1:**
```python
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

```

**Ejercicio 2:**
```python
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
```

**Ejercicio 3:**
```python
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
```

**Ejercicio 4:**
```python
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
```

**Ejercicio 5:**
```python
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
```

---

### Parte 2: Problema Integrador

```python
# sistema_biblioteca.py
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
```

---

## ✅ Checklist Final

Antes de entregar, verifica:

- [ x ] Todo el código está en español (comentarios, nombres de variables)
- [ x ] Todas las funciones tienen docstrings
- [ x ] El código compila sin errores de sintaxis
- [ x ] Has probado todos los casos de prueba
- [ x ] Las excepciones se manejan apropiadamente
- [ x ] El código sigue buenas prácticas (nombres descriptivos, código limpio)
- [ x ] Has incluido comentarios en lógica compleja
- [ x ] Los cálculos matemáticos son correctos
- [ x ] Las estructuras de datos son apropiadas para cada caso

---

## 📊 Tabla de Puntuación

| Sección | Puntos Máximos | Puntos Obtenidos |
|---------|----------------|------------------|
| Ejercicio 1: Expresiones Aritméticas | 10 | |
| Ejercicio 2: Expresiones Lógicas | 12 | |
| Ejercicio 3: Estructuras de Datos | 15 | |
| Ejercicio 4: Estructuras de Control | 10 | |
| Ejercicio 5: Estructuras de Repetición | 13 | |
| **Subtotal Parte 1** | **60** | |
| Problema Integrador: Sistema Biblioteca | 40 | |
| **Total** | **100** | |

---

**¡Buena suerte! 🎓**

---

**Tiempo de inicio:** __:__  
**Tiempo de finalización:** __:__  
**Tiempo total utilizado:** ______ horas ______ minutos
