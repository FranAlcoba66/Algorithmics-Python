def sort_by_frequency(arr):
    """
    CONSIGNA: Ordenar elementos de un array por frecuencia
    
    Dada una lista de números, devuelve una nueva lista donde los elementos
    están ordenados por su frecuencia de aparición en orden descendente.
    Si dos números tienen la misma frecuencia, ordena por valor en orden ascendente.
    
    Ejemplo:
    Input: [1, 1, 1, 2, 2, 3]
    Output: [1, 2, 3]  (1 aparece 3 veces, 2 aparece 2 veces, 3 aparece 1 vez)
    
    Input: [2, 3, 1, 3, 2]
    Output: [3, 2, 1]  (3 y 2 aparecen 2 veces, 1 aparece 1 vez)
    """
    # 1. Contar ocurrencias
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1

    # 2. Ordenar por:
    #    - frecuencia descendente
    #    - valor ascendente (si hay empate)
    result = sorted(
        freq.items(),
        key=lambda x: (-x[1], x[0])
    )

    # 3. Devolver solo los valores
    return [value for value, _ in result]



def binary_search(array, target):
    """
    CONSIGNA: Implementar búsqueda binaria
    
    Dado un array ORDENADO y un valor objetivo, encuentra el índice donde se
    encuentra ese valor usando búsqueda binaria.
    Si el valor no existe, devuelve -1 o el índice donde debería estar.
    
    Complejidad: O(log n)
    
    Ejemplo:
    Input: array = [1, 3, 5, 7, 9, 11], target = 7
    Output: 3
    
    Input: array = [1, 3, 5, 7, 9, 11], target = 6
    Output: -1 (no encontrado)
    """

    left = 0
    right= len(array) - 1

    while left <= right:
        mid =( left + right ) // 2

        if  array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid +1
        else:
            right = mid- 1

    return -1


list = [1, 3, 5, 7, 9, 11]
target =7


def romanToInt(s: str) -> int:
    """
    CONSIGNA: Convertir números romanos a enteros
    
    Dado un string con números romanos, convierte a su equivalente decimal.
    
    Tabla de valores:
    I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    
    Regla especial: Si un número menor aparece antes de uno mayor, se resta.
    Ejemplos:
    - IV = 4 (5 - 1)
    - IX = 9 (10 - 1)
    - XL = 40 (50 - 10)
    
    Ejemplo:
    Input: "III" -> Output: 3
    Input: "LVIII" -> Output: 58 (50 + 5 + 3)
    Input: "MCMXCIV" -> Output: 1994 (1000 + 900 + 90 + 4)
    """
    # Diccionario con los valores definidos en la tabla
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
        # Si el valor actual es menor al siguiente, se resta (regla de sustracción)
        if i < n - 1 and valores[s[i]] < valores[s[i+1]]:
            total -= valores[s[i]]
        else:
            # Caso contrario, se suma el valor
            total += valores[s[i]]
            
    return total

# --- PRINTS CON LOS EJEMPLOS DE LA CONSIGNA ---

# Ejemplo 1: "III"
# Explicación: III = 3
# print(f"Input: s = 'III' -> Output: {romanToInt('III')}")

# Ejemplo 2: "LVIII"
# Explicación: L = 50, V = 5, III = 3
# print(f"Input: s = 'LVIII' -> Output: {romanToInt('LVIII')}")

# Ejemplo extra con sustracción: "MCMXCIV"
# Explicación: M = 1000, CM = 900, XC = 90, IV = 4
# print(f"Input: s = 'MCMXCIV' -> Output: {romanToInt('MCMXCIV')}")




def two_sum(nums, target):
    """
    CONSIGNA: Encontrar dos números que sumen un valor objetivo
    
    Dado un array de números enteros y un número objetivo, encuentra los ÍNDICES
    de dos números diferentes cuya suma sea igual al objetivo.
    
    Restricciones:
    - No puedes usar el mismo elemento dos veces
    - Puedes devolver los índices en cualquier orden
    
    Complejidad óptima: O(n)
    
    Ejemplo:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]  (porque nums[0] + nums[1] = 2 + 7 = 9)
    
    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]  (porque nums[1] + nums[2] = 2 + 4 = 6)
    """

    seen ={}
    for index, value in enumerate(nums):
        complement = target -value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index


# print(two_sum( [2,7,11,15], 9  ) )


def count_bananas(string):
    """
    CONSIGNA: Contar cuántas palabras "BANANA" se pueden formar
    
    Dado un string con caracteres, cuenta cuántas palabras completas "BANANA"
    se pueden formar usando los caracteres disponibles.
    
    Cada "BANANA" requiere:
    - 1 'B'
    - 3 'A'
    - 2 'N'
    
    Ejemplo:
    Input: 'BBANANA'
    Conteo: B=2, A=3, N=2
    Output: 1  (puedes hacer 1 BANANA completa)
    
    Input: 'BBAAANNN'
    Conteo: B=2, A=3, N=3
    Output: 1  (limitado por las 'A': 3/3 = 1)
    
    Input: 'BBBAAANNNAA'
    Conteo: B=3, A=5, N=3
    Output: 1  (limitado por las 'B': 3/1 = 3, pero por 'N': 3/2 = 1)
    """

    counter = {}

    for ch in string:
        if ch == 'B'  or  ch == 'A'  or ch == 'N'  :
            counter[ch] = counter.get(ch, 0) + 1

    b = counter.get('B', 0) // 1
    a  = counter.get('A', 0) // 3
    n = counter.get('N', 0) // 2

    return min(b,a,n)




input = 'BBANANA'
# print(count_bananas(input))



def is_valid(string: str):
    """
    CONSIGNA: Validar que los paréntesis/brackets/llaves estén balanceados
    
    Dado un string que contiene caracteres y símbolos de agrupación,
    verifica que todos los paréntesis (), corchetes [] y llaves {} estén:
    1. Correctamente abiertos y cerrados
    2. En el orden correcto (no pueden cruzarse)
    
    Retorna:
    - True si están válidos/balanceados
    - False si no lo están
    
    Ejemplo:
    Input: "()"
    Output: True
    
    Input: "([{}])"
    Output: True
    
    Input: "([)]"
    Output: False  (se cruzan, corchete se cierra antes que paréntesis)
    
    Input: "{"
    Output: False  (no se cierra)
    """
    stack = []
    pairs = {'{': '}', '[': ']', '(': ')'}
    closers = set(pairs.values())


    for ch in string:
        if ch in pairs:
            stack.append(ch)
        elif ch in closers:
            if not stack or pairs[stack.pop()] != ch:
                return False

    return not stack




"""
CONSIGNA:
Dado un arreglo de enteros 'nums' ordenado de forma ascendente, devuelve
un nuevo arreglo que contenga los cuadrados de cada número,
también ordenados de forma ascendente.

Restricción: Intenta resolverlo con una complejidad de tiempo O(n).

Ejemplos:
- Input: [-4, -1, 0, 3, 10] -> Output: [0, 1, 9, 16, 100] 
- Input: [-7, -3, 2, 3, 11] -> Output: [4, 9, 9, 49, 121] 
"""
from typing import List

def calculate_squares(nums: List[int]) -> List[int]:
    n= len(nums)
    result =[0] * n

    left = 0
    right = n-1
    for i in range(n-1,-1,-1):
        if  abs(nums[left])  > abs(nums[right]) :
            result[i] = abs(nums[left])**2
            left +=1

        else:
            result[i] = abs(nums[right])**2
            right -=1

    return result

# Prueba esto en tu VS Code:
test_1 = [-4, -1, 0, 3, 10]
# print(f"Resultado esperado [0, 1, 9, 16, 100]")
# print(f"Tu resultado: {calculate_squares(test_1)}")





"""
CONSIGNA:
Realiza la compresión de una cadena siguiendo estas reglas:
1. Usa el conteo de caracteres repetidos (ej: "aab" -> "a2b1"). [cite: 29, 30]
2. Si la cadena comprimida NO es más corta que la original,
   debe retornar la cadena original. [cite: 31]

Ejemplos:
- Input: "aabcccccaaa" -> Output: "a2b1c5a3" [cite: 33, 34]
- Input: "abc" -> Output: "abc" (porque "a1b1c1" es más largo) [cite: 35, 36, 37]
"""
from collections import Counter
def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed_list = []
    count = 1
    
    # Iterar desde el segundo carácter hasta el final
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed_list.append(s[i-1] + str(count))
            count = 1
            
    # Agregar el último grupo
    compressed_list.append(s[-1] + str(count))
    
    compressed_str = "".join(compressed_list)
    
    # Retorna la original si la comprimida no es más corta
    return compressed_str if len(compressed_str) < len(s) else s

# Espacio para pruebas:
# print(f"Resultado: {compress_string('aabcccccaaa')}")  # Esperado: a2b1c5a3
# print(f"Resultado: {compress_string('abc')}")          # Esperado: abc



def binary_search(array, target):
    """
    CONSIGNA: Búsqueda Binaria (Versión con trazas)
    
    Busca un elemento en un array ordenado dividiendo el espacio de búsqueda a la mitad.

    
    Ejemplo:
    Input: array = [1, 3, 5, 7, 9], target = 3
    Output: 1 (índice del valor 3)
    """

    left = 0
    right = len(array) -1

    while left <= right:
        mid = (left + right )// 2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return -1 # Retorna -1 si el elemento no se encuentra

# array = [1,3,5,7,9,8, 10] # Este array no está ordenado, lo que viola la precondición de binary_search
# target =3
# print(f"Resultado: {binary_search(array,target)}")


def fibonacci_iterative(n):
    """
    CONSIGNA: Calcular Fibonacci de forma iterativa
    
    Calcula el n-ésimo número de la secuencia de Fibonacci sin usar recursión.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    
    Ejemplo:
    Input: n = 5
    Output: 5 (0, 1, 1, 2, 3, 5)
    """
    if n<2:
        return n

    prev= 0
    curr =1

    for _ in range(2, n+1):
        prev, curr = curr, prev + curr

    return curr
# Example usage:
# print(f"The 10th Fibonacci number is: {fibonacci_iterative(18)}")
# print(f"The 5th Fibonacci number is: {fibonacci_iterative(5)}")



def fibonacci_memoized(n, memo=None):
    """
    CONSIGNA: Calcular Fibonacci con Memoización (Recursivo)
    
    Calcula el n-ésimo número de Fibonacci usando recursión optimizada 
    con un diccionario (memo) para guardar resultados previos.
    
    Ejemplo:
    Input: n = 10
    Output: 55
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <2:
        return n

    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
 
    return memo[n]


# print(fibonacci_memoized(18))



from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    """
    CONSIGNA: Plantar flores sin adyacentes
    
    Determina si se pueden plantar 'n' flores nuevas en un cantero (array de 0s y 1s)
    sin violar la regla de que no pueden haber dos flores seguidas (no 1s adyacentes).
    
    Ejemplos:
    Input: flowerbed = [1,0,0,0,1], n = 1 -> Output: True
    Input: flowerbed = [1,0,0,0,1], n = 2 -> Output: False
    """
    flowerbed = [0] + flowerbed + [0]

    counter =0

    for i in range(1,len(flowerbed)-1):
        if flowerbed[i] == 0 and flowerbed[i-1] == 0  and flowerbed[i+1] == 0:
            flowerbed[i] =1
            counter+=1

    return counter >= n

# ======================
# Casos para probar
# ======================

print(canPlaceFlowers([1,0,0,0,0,1], 1))  # True
print(canPlaceFlowers([1,0,0,0,0,1], 2))  # False
print(canPlaceFlowers([0,0,0,0,0], 2))    # True
print(canPlaceFlowers([1,0,1,0,1,0,1], 1))# False


# ==========================================
# NUEVOS EJERCICIOS: Listas Enlazadas y Árboles
# ==========================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    """
    CONSIGNA: Invertir Lista Enlazada
    
    Dada la cabeza de una lista enlazada simple, inviértela y devuelve la nueva cabeza.
    
    Ejemplo:
    Input: 1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1
    """
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

def print_list(head):
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    return " -> ".join(vals)

# --- Pruebas Lista Enlazada ---
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(f"\nLista Original: {print_list(l1)}") 
reversed_head = reverse_linked_list(l1)
print(f"Lista Invertida: {print_list(reversed_head)}")


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth_binary_tree(root: TreeNode) -> int:
    """
    CONSIGNA: Profundidad Máxima de Árbol Binario
    
    Dada la raíz de un árbol binario, devuelve su profundidad máxima.
    La profundidad máxima es el número de nodos a lo largo del camino más largo
    desde el nodo raíz hasta el nodo hoja más lejano.
    
    Ejemplo:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    """
    if not root:
        return 0
    
    left_depth = max_depth_binary_tree(root.left)
    right_depth = max_depth_binary_tree(root.right)
    
    return max(left_depth, right_depth) + 1

# --- Pruebas Árbol ---
#       3
#      / \
#     9  20
#       /  \
#      15   7
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(f"Profundidad del árbol: {max_depth_binary_tree(tree)}") # Esperado: 3


