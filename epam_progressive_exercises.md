# Ejercicios Progresivos para Dominar el Ejercicio EPAM

## Nivel 1: Conceptos Básicos con Listas y Diccionarios

### Ejercicio 1.1: Acceder y filtrar datos básicos
```python
# Dado este listado de ventas simple:
sales = [
    {"product": "A", "price": 10},
    {"product": "B", "price": 20},
    {"product": "A", "price": 15},
]


# TODO: Filtra solo las ventas del producto "A"
# Resultado esperado: [{"producto": "A", "precio": 10}, {"producto": "A", "precio": 15}]
```

### Ejercicio 1.2: Calcular promedio simple
```python
prices = [10, 20, 15, 25]

# TODO: Calcula el promedio de estos precios
# Resultado esperado: 17.5
```

### Ejercicio 1.3: Filtrar y promediar
```python
sales = [
    {"store": "T1", "price": 10},
    {"store": "T2", "price": 20},
    {"store": "T1", "price": 15},
]

# TODO: Calcula el promedio de precios para tienda "T1"
# Resultado esperado: 12.5
```

---

## Nivel 2: Trabajar con Múltiples Filtros

### Ejercicio 2.1: Dos filtros (producto y tienda)
```python
sales = [
    {"product": "A", "store": "T1", "price": 10},
    {"product": "A", "store": "T2", "price": 20},
    {"product": "B", "store": "T1", "price": 15},
    {"product": "A", "store": "T1", "price": 12},
]

# TODO: Filtra ventas del producto "A" en tienda "T1"
# Resultado esperado: [{"product": "A", "store": "T1", "price": 10}, 
#                      {"product": "A", "store": "T1", "price": 12}]
```

### Ejercicio 2.2: Filtrar con listas de valores
```python
sales = [
    {"product": "A", "store": "T1", "price": 10},
    {"product": "B", "store": "T2", "price": 20},
    {"product": "C", "store": "T1", "price": 15},
    {"product": "A", "store": "T3", "price": 12},
]

products_to_search = ["A", "C"]
stores_to_search = ["T1"]

# TODO: Filtra ventas donde product esté en products_to_search 
#       Y store esté en stores_to_search
# Resultado esperado: [{"product": "A", "store": "T1", "price": 10},
#                      {"product": "C", "store": "T1", "price": 15}]
```

### Ejercicio 2.3: Agrupar y promediar por producto
```python
sales = [
    {"product": "A", "store": "T1", "price": 10},
    {"product": "B", "store": "T2", "price": 20},
    {"product": "A", "store": "T2", "price": 30},
    {"product": "B", "store": "T1", "price": 15},
]

# TODO: Crea un diccionario con el promedio de precio por producto
# Resultado esperado: {"A": 20.0, "B": 17.5}
```

---

## Nivel 3: Trabajar con Timestamps y Fechas

### Ejercicio 3.1: Convertir timestamp a fecha
```python
from datetime import datetime

timestamp_ms = 1672531200000  # 2023-01-01 00:00:00 UTC

# TODO: Convierte este timestamp (en milisegundos) a fecha ISO format
# Resultado esperado: "2023-01-01"
```

### Ejercicio 3.2: Filtrar por rango de fechas
```python
from datetime import datetime

sales = [
    {"product": "A", "price": 10, "timestamp": 1672531200000},  # 2023-01-01
    {"product": "A", "price": 20, "timestamp": 1672617600000},  # 2023-01-02
    {"product": "A", "price": 30, "timestamp": 1672704000000},  # 2023-01-03
]

days_to_filter = ["2023-01-01", "2023-01-02"]

# TODO: Filtra ventas cuya fecha esté en days_to_filter
# Resultado esperado: primeras dos ventas
```

---

## Nivel 4: Agregar Todo Junto

### Ejercicio 4.1: Filtrar múltiples criterios con timestamps
```python
sales = [
    {"product": "A", "store": "T1", "price": 10, "timestamp": 1672531200000},
    {"product": "A", "store": "T2", "price": 20, "timestamp": 1672617600000},
    {"product": "B", "store": "T1", "price": 15, "timestamp": 1672531200000},
]

products_to_search = ["A"]
stores_to_search = ["T1", "T2"]
days_to_filter = ["2023-01-01"]

# TODO: Filtra y calcula promedio de precio para:
#       - productos en products_to_search
#       - tiendas en stores_to_search
#       - fechas en days_to_filter
# Resultado esperado: (promedio de la primera venta = 10.0)
```

### Ejercicio 4.2: Retornar resultado en formato de diccionario
```python
sales = [
    {"product": "A", "store": "T1", "price": 10, "timestamp": 1672531200000},
    {"product": "A", "store": "T2", "price": 20, "timestamp": 1672617600000},
    {"product": "B", "store": "T1", "price": 30, "timestamp": 1672704000000},
]

products_to_search = ["A", "B"]
stores_to_search = ["T1"]
days_to_filter = ["2023-01-01", "2023-01-03"]

# TODO: Retorna un diccionario con el precio promedio por producto
# Resultado esperado: {"A": 10.0, "B": 30.0}
```

---

## Nivel 5: El Ejercicio Completo (EPAM)

Una vez domines los ejercicios anteriores, estarás listo para:

1. **Consumir datos** de la API (la función `sales(day)`)
2. **Filtrar** por múltiples criterios
3. **Agrupar y calcular** promedios
4. **Retornar** el resultado en el formato esperado

Estructura sugerida:
```python
def product_avg_price(product_ids: list, store_ids: list, days: list) -> Dict:
    # Paso 1: Obtener todos los datos de los días especificados
    # Paso 2: Filtrar por productos y tiendas
    # Paso 3: Agrupar por producto y calcular promedios
    # Paso 4: Retornar diccionario con resultados
```
