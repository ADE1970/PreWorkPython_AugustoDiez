'''
Crea una funcion que ante una entra de una lista de número nos devuelva la lista pero con todos los elementos en su valor absoluto
'''

def val_abs(cadena):
  for i in range(len(cadena)):
    cadena[i] = abs(cadena[i])
  return cadena

lista = [-3, 7, -9, 10]

listaABS = val_abs(lista)

print(f"Los valores en absoluto de la lista {lista}, son los siguientes {listaABS}")

