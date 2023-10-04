'''
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.
'''
def new_lis_unico(list):
  n_list = set(list)
  return n_list

prueba = [1, 2, 37, 2, 74, 37, 74, 347, 694, 12839, 25678]
n_prueba = new_lis_unico (prueba)
print(n_prueba)
