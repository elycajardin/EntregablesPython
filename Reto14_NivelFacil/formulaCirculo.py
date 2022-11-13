# función que calcule el área de un círculo a partir de su area
import math
def radio_circulo(a: float) -> float:
  radio_circulo= (math.sqrt(a))/math.pi
  print("El radio del circulo es ", (radio_circulo), "cm")