# Se definen las funciones en archivos separados y luego se importan al main para ser utilizadas

from formulaTriangulo import area_triangulo
print('Calculemos el área de un triangulo')
area_triangulo(input("Introduce la base en cm: "), input("Introduce la altura en cm: "))

from formulaCirculo import area_circulo
print('Y ahora, calculemos el área de un circulo')
area_circulo(input("Introduce el radio en cm: "))