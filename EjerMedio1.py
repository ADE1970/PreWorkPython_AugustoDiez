'''
 Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.
'''

def fibonacci_iterativo(n):
    fibonacci = []
    a , b = 0 , 1
    
    for _ in range(n):
        fibonacci.append(a)
        a , b = b, a + b
    return fibonacci

n = 10
lista = fibonacci_iterativo(n)
print(lista)