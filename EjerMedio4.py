'''
4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.
'''

def sum_dig(n):
  sum = 0
  n_tex = str(n)
  for digito in n_tex:
    sum = sum + int(digito)
  return sum
  
valor = int(input("Ingresa un numero: "))
sum_valor = sum_dig(valor)
print(f"La suma de todos los digitos del numero {valor} es {sum_valor}")

