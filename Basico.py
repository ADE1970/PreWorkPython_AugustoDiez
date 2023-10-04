''' 
Dado un numero mediante funciones, nos dice si es par o impar, calcula el factorial
'''
def es_par(n):
  if n % 2 == 0:
    return True
  else:
    return False
  
def su_factorial(n):
  factorial = 1
  for i in range(1, n+1):
    factorial *= i
  return factorial




Numero = int(input("Ingresa un número: "))
print (f"El numero que has elegido es: {Numero}")
if es_par(Numero):
  print(f"{Numero} es un número par")
else:
  print(f"{Numero} es un número impar")

print(f"y su factorial es ", su_factorial(Numero))
