'''
Variables y Operadores
1. Ejercicio: Crea una variable llamada nombre y asígnale tu nombre como valor.
Luego, imprime la variable.
2. Ejercicio: Crea dos variables, a y b , y asígnales los valores 5 y 10
respectivamente. Luego, imprime la suma de a y b .
3. Ejercicio: Calcula el área de un triángulo con base 10 y altura 5.
4. Ejercicio: Calcula el resto de dividir 17 entre 3.
'''
nombre = 'Augusto'
print (nombre)

a = 5
b = 10
suma = a + b
print (suma)

base = 10
altura = 5
area = (base * altura) / 2
print (f"El área del triángulo con base {base} y altura {altura} es: {area}")

dividendo = 17
divisor = 3
resultado = dividendo / divisor
entero = int(resultado)
resto = int( (resultado - entero) * divisor)
print (f"El resto, de dividir {dividendo} entre {divisor} es: {resto}")

