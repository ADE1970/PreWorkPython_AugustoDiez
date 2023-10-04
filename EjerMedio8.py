'''
: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
'''
def div_num(num):
    divisores = []
    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)
    return divisores

def sum_lista(lista):
    suma = 0
    for valor in lista:
        suma = suma + int(valor)
    return suma

Va = int(input("Ingreasa el número que quieres comprobar si es perfecto: "))
divA = div_num(Va)
print(divA)
suma_div = sum_lista(divA)
print(suma_div)
if Va == suma_div:
    print(f"El numero {Va} es perfecto, ya que la suma de sus divisores {divA} es igual al valor del número")
else:
    print(f"El numero {Va} no es perfecto, ya que la suma de sus divisores {divA} es igual a {suma_div} y no coincide con el valor {Va}")
