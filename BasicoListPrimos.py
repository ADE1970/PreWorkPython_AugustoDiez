'''
Dado un numero, chequea si es primo y elabora la lista de primos hasta el
'''

def es_primo(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def lista_de_primos_hasta(num):
    primos = []
    for i in range(2, num + 1):
        if es_primo(i):
            primos.append(i)
    return primos

valor = int(input("Ingrese un número: "))

if es_primo(valor):
    print(f"{valor} es un número primo.")
else:
    print(f"{valor} no es un número primo.")

primos_hasta_numero = lista_de_primos_hasta(valor)
print(f"Lista de números primos hasta {valor}: {primos_hasta_numero}")
