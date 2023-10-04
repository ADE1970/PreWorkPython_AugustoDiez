'''
De una lista de números, devuelve el máximo mediante una función
'''

def encontrar_mayor(lista):
    maximo = lista[0]  # Suponemos que el primer número es el mayor inicialmente
    for numero in lista:
        if numero > maximo:
            maximo = numero  # Actualizamos el número mayor si encontramos uno más grande
    return maximo

lista = [310, 5, 20, 8, 15]
mayor = encontrar_mayor(lista)
print(f"El número mayor en la lista {lista} es: {mayor}")
