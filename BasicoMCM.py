'''
Define una funcion que de el Minimo Comun Multiplo de dos números introducidos
'''

def fun_MCM(a,b):
  if a == 0 or b == 0:
    return 0
  else:
   maximo = max(a , b)
  while True:
    if maximo % a == 0 and maximo % b == 0:
      return maximo
    maximo +=1

num1 = int(input("Introduce el primer número:"))
num2 = int(input("Introduce el segundo número:"))

resultado = fun_MCM(num1,num2)

print(f"El mínimo comun multiplo de {num1} y de {num2} es {resultado}")