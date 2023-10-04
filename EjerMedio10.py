'''
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas)
'''
def lista_comun(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    comun = list(conjunto1 & conjunto2)
    return comun

list1 = input("Ingresa la primera lista: ")
list2 = input("Ingresa la segunda lista: ")

list_comun = lista_comun(list1, list2)
print(list_comun)