'''
Dado un numero decir la cantidad de digitos que tiene
'''

def cantidad(n):
  cadena = str(n)
  longitud = len(cadena)
  return longitud

Numero = int(input("Ingresa un número: "))
print (cantidad(Numero))
