# Consignas para resolver — OOP y funciones en Python

Resuelve las siguientes consignas implementando funciones, clases y ejemplos en Python. Cada ejercicio debe incluir una breve demostración en un bloque `if __name__ == "__main__"` o ejemplos unitarios sencillos.

1. Función `c(x)`
   - Implementar `c(x)` que devuelva el doble de `x`.
   - Criterio: `c(3)` debe devolver `6`.

2. Clase y método
   - Crear `MyClass` con un constructor que reciba `name` y un método `greet()` que devuelva un saludo.
   - Ejemplo: `MyClass("Fran").greet()` -> `"Hola, Fran!"`.

3. Repositorio en memoria
   - Implementar `UserRepository` con métodos: `add(name) -> id`, `get_by_id(id) -> name` y `list_all() -> list`.
   - Debe manejar ids incrementales y almacenar datos en una estructura interna (ej. diccionario).

4. Servicio
   - Implementar `UserService` que reciba una instancia de `UserRepository` y exponga `create_user(name)` y `get_user(id)`.

5. Controlador / Router (simulado)
   - Escribir una función `user_controller_create(name, service)` que use el servicio para crear un usuario y devuelva el id.

6. Decorador `timed`
   - Implementar un decorador `@timed` que mida y muestre el tiempo de ejecución de la función decorada.

7. List comprehension
   - Crear una lista por comprensión `squares` con los cuadrados de 0 a 4.

8. Generador
   - Implementar `count_up(n)` que haga `yield` de 0 a `n-1`.

9. Closure
   - Implementar `make_multiplier(factor)` que devuelva una función que multiplique su argumento por `factor`.

10. Lambda
    - Definir `adder = lambda a, b: a + b` y mostrar un ejemplo de uso.

11. Métodos mágicos
    - Implementar una clase `Point` con `__repr__`, `__add__` y `__eq__`.
    - Ejemplo: `Point(1,2) + Point(3,4) -> Point(4,6)`.

---

Notas y criterios de aceptación
- Cada punto debe poder ejecutarse de forma independiente dentro de un script (bloque `__main__`) o mediante pequeñas pruebas.
- Mantener el código claro y con nombres descriptivos.
- No es necesario usar frameworks externos; usar solo la librería estándar de Python.

Opcional
- Añadir pequeños docstrings a funciones y clases.
- Añadir ejemplos de uso en comentarios o en el bloque `__main__`.

Archivo relacionado: [OOP.py](OOP.py)
