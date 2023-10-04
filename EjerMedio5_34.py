'''
5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.
'''
def  cont_voc(texto):
  vocales = "aeiouAEIOU"
  contador = 0
  for caracter in texto:
    if caracter in vocales:
      contador = contador +1
  return contador
  
texto = input("introduce el texto que quieras comprobar las vocales: ")
suma_vocales = cont_voc(texto)

print(f"En el texto '{texto}', el número de vocales es {suma_vocales}")
