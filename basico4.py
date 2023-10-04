'''
Crear función que dado un numero, sume los digitos de ese numero
en una lista, y luego otra función que sume todos los numeros de la lista
'''

def numero_a_lista(numero):
    lista_digitos = []
    numero_absoluto = abs(numero)  # Tomamos el valor absoluto del número para manejar números negativos
    while numero_absoluto > 0:
        digito = numero_absoluto % 10  # Obtenemos el último dígito
        lista_digitos.insert(0, digito)  # Insertamos el dígito al principio de la lista
        numero_absoluto //= 10  # Eliminamos el último dígito
    return lista_digitos

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

valor = int(input("Introduce un número: "))
lista = numero_a_lista(valor)
print("El número convertido en lista de dígitos es:", lista)
m = suma_lista(lista)
print(f"y la suma de todos los dígitos del numero {valor} es {m}")