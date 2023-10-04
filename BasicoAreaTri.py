def area_triangulo(a,b):
  area = (a * b)/2
  return area

base = int(input("Introduce la base del triangulo"))
altura = int(input("Introduce la altura del triangulo"))
area = area_triangulo(base, altura)
print(f"El area de un triangulo de base {base} y altura {altura} es {area}")
