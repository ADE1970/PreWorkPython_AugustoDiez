'''
Crea una funcion que ante la entrada de un numero diga si es positivo o negativo
'''

def n_mayor0(num):
  if num >= 0:
    return True
  else:
    return False
  
valor = int(input("Introduce un numero: "))

if n_mayor0(valor):
  print(f"El numero {valor} es positivo")
else:
  print(f"El numero {valor} es negativo")
  