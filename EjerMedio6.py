'''
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
'''

def n_elemen_lista(n,cadena):
  return cadena[:n] 

lista = list(input("Introduce la lista: "))
numero = int(input("Introduce el número: "))

n_lista = n_elemen_lista(numero,lista)
print(n_lista)