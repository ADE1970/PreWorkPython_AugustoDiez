'''
2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores
'''

''' Primero creo una función que de la lista de divisores de un numero'''
def div_num(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores
Va = int(input("Ingreasa el primer número: "))

divA = div_num(Va)
print(f"Los divisores del numero {Va} son: {divA}")