'''
Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.
'''

def suma(a,b):
  return a + b
print (suma(4,0.7))


def factorial(n):
    if n < 1:
        return "Los numeros negativos y el cero no tienen factorial"
    elif n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
n = 10
resultado = factorial(n)
print(f"El factorial de {n} es: {resultado}")
