'''
Definir una funcion que reciba una lista de números y retorne su suma
'''
def SumList (lista):
  suma = 0
  for numero in lista:
    suma += numero
  return suma
  
lista = [1,1,1,1,1,1,1]
resultado = SumList(lista)
print (resultado)
