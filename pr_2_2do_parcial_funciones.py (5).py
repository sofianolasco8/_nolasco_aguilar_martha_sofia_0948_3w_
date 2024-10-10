print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w ")
print(" ")
import math
#crea una funsion para sacar el radio de un circulo
def area_circulo(radio):
    return math.pi * radio ** 2  # A = π * r^2
#crea una funsion para sacar el radio y la altura  de el circulo
def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura  # V = A * h

# Pide al usuario el radio y la altura
radio = float(input("ingresa el radio del círculo: "))
altura = float(input("ingresa la altura del cilindro: "))

# Calcula el área y el volumen
area = area_circulo(radio)
volumen = volumen_cilindro(radio, altura)

# Muestra los resultados
print("Área del círculo ", round(area, 2))
print("Volumen del cilindro", round(volumen, 2))