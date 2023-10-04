'''
Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''

a = -2
if a > 0 :
  print (f"El numero {a} es positivo")
else :
  print (f"El numero {a} es negativo")

b = 12
prueba = b/2
decimal = prueba - int (prueba)
if decimal == 0 :
  print (f"El numero {b} es un numero par")
else :
  print (f"El numero {b} es un numero impar")

numero1 = 0.5
numero2 = 0
numero3 = -5
NumeroMayor=numero1

if numero2 > NumeroMayor :
  NumeroMayor = numero2
if numero3 > NumeroMayor :
  NumeroMayor = numero3

print (f"El numero mayor es {NumeroMayor}")




