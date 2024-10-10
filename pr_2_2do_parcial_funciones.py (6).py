print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w")
print(" ")
def es_vocal(caracter):
    """Devuelve True si el carácter es una vocal, de lo contrario devuelve False."""
    vocales = 'aeiouAEIOU'
    return caracter in vocales

if __name__ == "__main__":
    caracter = input("Introduce un carácter: ")
    
    if len(caracter) == 1:  # Asegurarse de que se introdujo un solo carácter
        resultado = es_vocal(caracter)
        if resultado:
            print(f"El carácter '{caracter}' es una vocal.")
        else:
            print(f"El carácter '{caracter}' no es una vocal.")
    else:
        print("Por favor, introduce solo un carácter.")
