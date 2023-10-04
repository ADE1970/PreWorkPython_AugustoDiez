'''
Define una funcion que recige una cadena de texto y la retorna a la reversa
'''

def cadena_reversa(cadena):
  cadena_reversa = cadena [::-1] #esta función la he cogido de chatgpt
  return cadena_reversa

texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme ..."
reverso = cadena_reversa (texto)
print(reverso)
