# 🚀 Ruta de Aprendizaje: Python y Algoritmia (De Cero a Héroe)

Progresión estructurada para dominar Python y algoritmia. Completa cada sección antes de pasar a la siguiente.

---

## **NIVEL 1: FUNDAMENTOS DE PYTHON**

### 1.1 Variables y Entrada/Salida

1. **Doble de un número**: Lee un número y devuelve su doble
   - Entrada: `5`
   - Salida: `10`

2. **Mayor de dos números**: Lee dos números e imprime el mayor
   - Entrada: `10, 3`
   - Salida: `10`

3. **Clasificación de números**: Verifica si un número es positivo, negativo o cero
   - Entrada: `-5`
   - Salida: `"Negativo"`

### 1.2 Strings y Listas Básicas

4. **Invierte una cadena** (sin usar `[::-1]`)
   - Entrada: `"Hola"`
   - Salida: `"aloH"`
   - *Pista: usa un bucle*

5. **Cuenta vocales**: Cuenta cuántas vocales hay en un texto
   - Entrada: `"Hola Mundo"`
   - Salida: `3`

6. **Elemento mayor en lista**: Dada una lista, devuelve el elemento más grande
   - Entrada: `[3, 7, 2, 9, 1]`
   - Salida: `9`

### 1.3 Bucles

7. **Primeros números pares**: Imprime los primeros 10 números pares
   - Salida: `2, 4, 6, 8, 10, 12, 14, 16, 18, 20`

8. **Suma de naturales**: Calcula la suma de los primeros N números naturales
   - Entrada: `5`
   - Salida: `15` (1+2+3+4+5)

9. **Factorial**: Encuentra el factorial de un número
   - Entrada: `5`
   - Salida: `120` (5×4×3×2×1)

---

## **NIVEL 2: ESTRUCTURAS DE DATOS**

### 2.1 Listas y Arrays

10. **Búsqueda en lista**: Busca si un número existe en una lista
    - Entrada: `[1, 5, 9, 3], 9`
    - Salida: `True`

11. **Segundo mayor**: Encuentra el segundo número más grande en una lista
    - Entrada: `[10, 20, 5, 30, 15]`
    - Salida: `20`

12. **Eliminar duplicados** (sin usar `set()`)
    - Entrada: `[1, 2, 2, 3, 3, 3, 4]`
    - Salida: `[1, 2, 3, 4]`

13. **Rotar lista**: Rota una lista N posiciones a la derecha
    - Entrada: `[1, 2, 3, 4, 5], N=2`
    - Salida: `[4, 5, 1, 2, 3]`

### 2.2 Diccionarios

14. **Frecuencia de caracteres**: Cuenta la frecuencia de cada carácter en un string
    - Entrada: `"aabbcc"`
    - Salida: `{'a': 2, 'b': 2, 'c': 2}`

15. **Fusionar diccionarios**: Dados dos diccionarios, fusiónalos en uno solo
    - Entrada: `{'a': 1}, {'b': 2}`
    - Salida: `{'a': 1, 'b': 2}`

16. **Clave con mayor valor**: Encuentra la clave con el mayor valor en un diccionario
    - Entrada: `{'x': 10, 'y': 20, 'z': 5}`
    - Salida: `'y'`

### 2.3 Tuplas y Sets

17. **Pares pitagóricos**: Crea pares de números (x, y) donde x² + y² = 25
    - Salida: `(3, 4), (4, 3), (5, 0)` (u otros válidos)

18. **Intersección de listas**: Encuentra la intersección de dos listas
    - Entrada: `[1, 2, 3, 4], [3, 4, 5, 6]`
    - Salida: `[3, 4]`

19. **Diferencia de sets**: ¿Cuál es la diferencia entre dos conjuntos?
    - Entrada: `{1, 2, 3}, {2, 3, 4}`
    - Salida: `{1}` (elementos en el primero que no están en el segundo)

---

## **NIVEL 3: PENSAMIENTO ALGORÍTMICO**

### 3.1 Búsqueda

20. **Búsqueda Lineal**: Implementa un algoritmo que busque un elemento y devuelva su índice (-1 si no existe)
    - Entrada: `[2, 5, 8, 12], 8`
    - Salida: `2`

21. **Búsqueda Binaria**: Busca un número en una lista ordenada (muy eficiente)
    - Entrada: `[1, 3, 5, 7, 9, 11], 7`
    - Salida: `3`
    - *Nota: La lista está ordenada*

22. **Posición de inserción**: Encuentra el índice donde debería insertarse un número para mantener orden
    - Entrada: `[1, 3, 5, 7], 4`
    - Salida: `2` (entre 3 y 5)

### 3.2 Ordenamiento

23. **Bubble Sort**: Ordena una lista de mayor a menor
    - Entrada: `[5, 2, 8, 1, 9]`
    - Salida: `[9, 8, 5, 2, 1]`

24. **Selection Sort**: Implementa ordenamiento por selección
    - Entrada: `[64, 25, 12, 22, 11]`
    - Salida: `[11, 12, 22, 25, 64]`

25. **Ordenar combinado**: Ordena una lista de números y palabras conjuntamente (primero números, luego palabras)
    - Entrada: `['z', 5, 'a', 2, 'm']`
    - Salida: `[2, 5, 'a', 'm', 'z']`

### 3.3 Dos Punteros

26. **Two Sum (ordenado)**: Dados dos números en una lista ordenada que suman X, encuéntralos
    - Entrada: `[2, 7, 11, 15], target=9`
    - Salida: `(2, 7)`

27. **Invertir lista (sin memoria extra)**: Invierte una lista sin usar memoria extra
    - Entrada: `[1, 2, 3, 4, 5]`
    - Salida: `[5, 4, 3, 2, 1]`

28. **Palíndromo en lista**: Encuentra si hay un palíndromo en una lista de caracteres
    - Entrada: `['a', 'b', 'a']`
    - Salida: `True`

---

## **NIVEL 4: RECURSIÓN Y BACKTRACKING**

### 4.1 Recursión Básica

29. **Potencia**: Calcula 2^N usando recursión
    - Entrada: `5`
    - Salida: `32`

30. **Suma recursiva**: Suma todos los números de una lista recursivamente
    - Entrada: `[1, 2, 3, 4, 5]`
    - Salida: `15`

31. **Invierte string (recursión)**: Invierte una cadena usando recursión
    - Entrada: `"Python"`
    - Salida: `"nohtyP"`

### 4.2 Problemas Clásicos

32. **Fibonacci**: Genera el N-ésimo número de Fibonacci
    - Entrada: `6`
    - Salida: `8` (0, 1, 1, 2, 3, 5, 8...)

33. **Torres de Hanoi**: Resuelve el problema con 3 discos
    - Imprime los movimientos necesarios

34. **Permutaciones de string**: Genera todas las permutaciones de una cadena
    - Entrada: `"ABC"`
    - Salida: `['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']`

### 4.3 Backtracking

35. **Combinaciones**: Genera todas las combinaciones de N números de M opciones
    - Entrada: `N=2, M=[1, 2, 3]`
    - Salida: `[[1, 2], [1, 3], [2, 3]]`

36. **N-Queens**: Resuelve el problema del N-Queens (al menos para N=4)
    - Encuentra una configuración válida donde las reinas no se atacan

---

## **NIVEL 5: PROGRAMACIÓN DINÁMICA**

### 5.1 Problemas Clásicos

37. **Monedas mínimas**: Número mínimo de monedas para hacer cantidad X
    - Entrada: `monedas=[1, 2, 5], cantidad=5`
    - Salida: `1` (una moneda de 5)

38. **Escaleras**: ¿De cuántas formas puedes subir N escalones (puedes subir 1 o 2 pasos)?
    - Entrada: `4`
    - Salida: `5` (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)

39. **Mochila 0/1**: Dada una capacidad, maximiza el valor con pesos dados
    - Entrada: `pesos=[2, 3, 4], valores=[3, 4, 5], capacidad=5`
    - Salida: `9` (máximo valor con peso ≤ 5)

### 5.2 Secuencias

40. **Subsecuencia común más larga (LCS)**: Encuentra la LCS entre dos strings
    - Entrada: `"abcde", "ace"`
    - Salida: `"ace"` (o su longitud: 3)

41. **Edición mínima**: Mínimo de operaciones para transformar string A en B
    - Entrada: `"cat", "dog"`
    - Salida: `3` (reemplazar 3 caracteres)

---

## **NIVEL 6: GRAFOS Y ÁRBOLES**

### 6.1 Representación

42. **Grafo como lista de adyacencia**: Representa un grafo como lista de adyacencia
    - Entrada: aristas `[(1,2), (2,3), (3,4)]`
    - Salida: `{1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}`

43. **Árbol binario**: Implementa un árbol binario básico con métodos de inserción

### 6.2 Recorridos

44. **DFS (Depth-First Search)**: Recorre un grafo en profundidad
    - Entrada: grafo, nodo inicial
    - Salida: orden de visita

45. **BFS (Breadth-First Search)**: Recorre un grafo en amplitud
    - Entrada: grafo, nodo inicial
    - Salida: orden de visita por niveles

46. **Recorridos de árbol**: Recorre un árbol binario en preorden, inorden y postorden
    - Salida: listas con elementos en cada orden

### 6.3 Algoritmos

47. **Camino más corto (Dijkstra)**: Encuentra el camino más corto en un grafo
    - Entrada: grafo con pesos, nodo inicio
    - Salida: distancias mínimas a todos los nodos

48. **Detectar ciclos**: Detecta si hay ciclos en un grafo
    - Entrada: grafo
    - Salida: `True` o `False`

49. **Validar BST**: ¿Es un árbol un Binary Search Tree válido?
    - Entrada: árbol
    - Salida: `True` o `False`

---

## **NIVEL 7: PROBLEMAS DE ENTREVISTA (LeetCode Easy/Medium)**

50. **Two Sum**: Encuentra dos números que sumen un objetivo
    - Entrada: `[2, 7, 11, 15], target=9`
    - Salida: `[0, 1]` (índices)

51. **Longest Substring**: Substring más largo sin caracteres repetidos
    - Entrada: `"abcabcbb"`
    - Salida: `3` (longitud de "abc")

52. **Merge Intervals**: Fusiona intervalos solapados
    - Entrada: `[[1,3], [2,6], [8,10], [15,18]]`
    - Salida: `[[1,6], [8,10], [15,18]]`

53. **Product of Array Except Self**: Calcula productos sin usar división
    - Entrada: `[1, 2, 3, 4]`
    - Salida: `[24, 12, 8, 6]` (producto de todos excepto el actual)

54. **Rotate Array**: Rota un array N posiciones
    - Entrada: `[1, 2, 3, 4, 5], k=2`
    - Salida: `[4, 5, 1, 2, 3]`

55. **Valid Parentheses**: ¿Los paréntesis están balanceados?
    - Entrada: `"()[]{}"`
    - Salida: `True`
    - Entrada: `"(]"`
    - Salida: `False`

---

## 📋 **Cómo Usar Esta Ruta**

1. **Comienza en Nivel 1** - No saltes niveles
2. **Resuelve 3-5 ejercicios por día** - Calidad > cantidad
3. **Usa un archivo Python diferente** para cada ejercicio
4. **NO mires soluciones** hasta intentar 20+ minutos
5. **Optimiza después** - Primero funciona, luego rápido

---

## 🎯 **Consejos para Entrevistas Algorítmicas**

- ✅ Entiende el problema antes de codear
- ✅ Explica tu enfoque en voz alta
- ✅ Prueba con ejemplos simples primero
- ✅ Escribe código limpio y con comentarios
- ✅ Analiza complejidad: O(n), O(n²), etc.
- ✅ Maneja casos especiales (vacío, un elemento, etc.)

---

## 📊 **Progresión de Complejidad**

| Nivel | Tópicos | Duración |
|-------|---------|----------|
| 1 | Fundamentos | 3-5 días |
| 2 | Estructuras de datos | 5-7 días |
| 3 | Algoritmia básica | 7-10 días |
| 4 | Recursión | 5-7 días |
| 5 | Programación dinámica | 10-14 días |
| 6 | Grafos y árboles | 14-21 días |
| 7 | Problemas reales | 21+ días |

**Total estimado: 2-3 meses de dedicación**

---

**¿Listo para comenzar? Puedo ayudarte revisando tus soluciones sin revelar la respuesta.**
