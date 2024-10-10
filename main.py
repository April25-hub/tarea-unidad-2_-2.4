print(" ")
print("Arzab Diaz April 3W 1173")
import math

def calcular_area_circulo(radio):
    """
    calcula el area de un circulo dado su radio.

    args:
        radio (float): el radio del circulo.

    returns:
        float: el area del circulo.
    """
    area = math.pi * (radio ** 2)
    return area

def calcular_volumen_cilindro(radio, altura):
    """
calcula el volumen de un cilindro dado su radio y altura.

    args:
        radio (float): el radio de la base del cilindro.
        altura (float): la altura del cilindro.

    Returns:
        float: El volumen del cilindro.
    """
    area_base = calcular_area_circulo(radio)  # Llama a la funcion para calcular el area
    volumen = area_base * altura
    return volumen

# Ejemplo de uso
radio = 5  # Radio del circulo y base del cilindro
altura = 10  # Altura del cilindro

area = calcular_area_circulo(radio)
volumen = calcular_volumen_cilindro(radio, altura)

print(f"El area del circulo con radio {radio} es: {area}")
print(f"El volumen del cilindro")
