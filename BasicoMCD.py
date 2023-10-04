'''
Crea una funcion que de el Maximo Comun Divisor de dos números
'''

''' Primero creo una función que de la lista de divisores de un numero'''
def div_num(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores

def numero_comun(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    comun = conjunto1.intersection(conjunto2)
    return comun

Va = int(input("Ingreasa el primer número: "))
Vb = int(input("Ingresa el segundo número: "))

divA = div_num(Va)
print(f"Los divisores del numero {Va} son: {divA}")

divB = div_num(Vb)
print(f"Los divisores del numero {Vb} son: {divB}")

ListComun = numero_comun(divA, divB)
print(f"La lista comun de divisores es {ListComun}")

MaxComDiv = max(ListComun)
print(f"El Maximo Comun Divisor del numero {Va} y del número {Vb} es el {MaxComDiv}")