'''
Define una funcion que ante la entrada de una palabra, determine el numero de letras que contiene
'''

def con_let(texto):
  conta = 0
  for letra in texto:
    if letra.isalpha(): #esta función la he buscado en chatgpt
      conta +=1
  return conta

palabra = input("Introduce una palabra:")
contador = con_let(palabra)
print (f"El numero de letras en el texto {palabra} es {contador}")
