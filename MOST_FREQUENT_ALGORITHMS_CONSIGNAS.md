# Consignas de Algoritmos Frecuentes

Este archivo documenta las consignas de los ejercicios incluidos en `most_frequent_algorythms.py`.

---

## 1. Ordenar por Frecuencia
**Función:** `sort_by_frequency(arr)`

Dada una lista de números, devuelve una nueva lista donde los elementos están ordenados por su frecuencia de aparición en **orden descendente**.
Si dos números tienen la misma frecuencia, ordénalos por valor en **orden ascendente**.

**Ejemplo:**
- Input: `[1, 1, 1, 2, 2, 3]` -> Output: `[1, 2, 3]` (1 aparece 3 veces, 2 aparece 2 veces, 3 aparece 1 vez)
- Input: `[2, 3, 1, 3, 2]` -> Output: `[3, 2, 1]` (3 y 2 aparecen 2 veces, 1 aparece 1 vez)

---

## 2. Búsqueda Binaria
**Función:** `binary_search(array, target)`

Dado un array **ORDENADO** y un valor objetivo, encuentra el índice donde se encuentra ese valor usando búsqueda binaria.
Si el valor no existe, devuelve -1.

**Complejidad:** `O(log n)`

**Ejemplo:**
- Input: array = `[1, 3, 5, 7, 9, 11]`, target = `7` -> Output: `3`
- Input: array = `[1, 3, 5, 7, 9, 11]`, target = `6` -> Output: `-1`

---

## 3. Romanos a Enteros
**Función:** `romanToInt(s)`

Dado un string con números romanos, conviértelo a su equivalente decimal.

**Tabla de valores:**
`I=1, V=5, X=10, L=50, C=100, D=500, M=1000`

**Regla especial:** Si un número menor aparece antes de uno mayor, se resta (ej. `IV = 4`, `IX = 9`).

**Ejemplo:**
- Input: `"III"` -> Output: `3`
- Input: `"LVIII"` -> Output: `58`
- Input: `"MCMXCIV"` -> Output: `1994`

---

## 4. Two Sum (Suma de Dos Números)
**Función:** `two_sum(nums, target)`

Dado un array de números enteros y un número objetivo, encuentra los **ÍNDICES** de dos números diferentes cuya suma sea igual al objetivo.

- No puedes usar el mismo elemento dos veces.
- Puedes devolver los índices en cualquier orden.
- **Complejidad óptima:** `O(n)`

**Ejemplo:**
- Input: `nums = [2, 7, 11, 15]`, target `9` -> Output: `[0, 1]` (porque `nums[0] + nums[1] = 9`)

---

## 5. Contar "BANANA"
**Función:** `count_bananas(string)`

Dado un string con caracteres, cuenta cuántas palabras completas "BANANA" se pueden formar.

**Requerimientos por palabra:**
- 1 'B'
- 3 'A'
- 2 'N'

**Ejemplo:**
- Input: `'BBANANA'` -> Output: `1`
- Input: `'BBAAANNN'` -> Output: `1` (Limitado por las A)

---

## 6. Validar Paréntesis
**Función:** `is_valid(string)`

Valida que los paréntesis `()`, corchetes `[]` y llaves `{}` estén balanceados y cerrados en el orden correcto.

**Ejemplo:**
- Input: `"()"` -> Output: `True`
- Input: `"([{}])"` -> Output: `True`
- Input: `"([)]"` -> Output: `False` (Se cruzan)

---

## 7. Cuadrados de un Array Ordenado
**Función:** `calculate_squares(nums)`

Dado un arreglo ordenado de forma ascendente (que puede tener negativos), devuelve un nuevo arreglo con los **cuadrados de cada número**, también ordenados ascendentemente.

- **Complejidad requerida:** `O(n)`

**Ejemplo:**
- Input: `[-4, -1, 0, 3, 10]` -> Output: `[0, 1, 9, 16, 100]`

---

## 8. Compresión de Cadenas
**Función:** `compress_string(s)`

Realiza la compresión básica de una cadena utilizando el conteo de caracteres repetidos.
Si la cadena comprimida NO es más pequeña que la original, debe devolver la original.

**Ejemplo:**
- Input: `"aabcccccaaa"` -> Output: `"a2b1c5a3"`
- Input: `"abc"` -> Output: `"abc"` (porque `a1b1c1` es más larga)

---

## 9. Fibonacci
**Iterativo:** `fibonacci_iterative(n)`
**Memoizado (Recursivo):** `fibonacci_memoized(n)`

Calcula el n-ésimo número de la secuencia de Fibonacci. `F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)`.

---

## 10. Plantar Flores
**Función:** `canPlaceFlowers(flowerbed, n)`

Determina si se pueden plantar `n` flores nuevas en un cantero (array de 0s y 1s) sin violar la regla de que **no puede haber flores adyacentes** (no `1`s seguidos).

**Ejemplo:**
- Input: `flowerbed = [1,0,0,0,1], n = 1` -> Output: `True`
- Input: `flowerbed = [1,0,0,0,1], n = 2` -> Output: `False`

---

## 11. Invertir Lista Enlazada
**Función:** `reverse_linked_list(head)`

Dada la cabeza de una lista enlazada simple, inviértela y devuelve la nueva cabeza.

**Estructura:**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

**Ejemplo:**
- Input: `1 -> 2 -> 3 -> 4 -> 5`
- Output: `5 -> 4 -> 3 -> 2 -> 1`

---

## 12. Profundidad Máxima de Árbol Binario
**Función:** `max_depth_binary_tree(root)`

Dada la raíz de un árbol binario, devuelve su profundidad máxima (número de nodos en el camino más largo de la raíz a una hoja).

**Estructura:**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Ejemplo:**
- Input: `root = [3,9,20,null,null,15,7]`
- Output: `3`
