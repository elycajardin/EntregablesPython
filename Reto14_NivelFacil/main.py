import math
from formulaCirculo import radio_circulo

print('Calculemos el volumen de un cilindro a partir del área de un círculo')
print('Primero, calculemos el radio del círculo')
radio_circulo(float(input("Introduce el área del circulo en cm2: ")))

from formulaCilindro import volumen_cilindro
print('Y ahora, podemos calcular el volumen del cilindro')

altura = float(input('Introduce la longitud del cilindro en cm: '))

volumen_cilindro(r = radio_circulo, a= altura)

## Pendiente de corregir formula