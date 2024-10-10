print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w ")
print(" ")

def calcular_factura(cantidad_sin, t_iva=21):#crea la funcion
    iva = cantidad_sin * (t_iva / 100)  # Calcula el IVA
    return cantidad_sin + iva  # Devuelve el total

# Solicita la cantidad sin IVA
cantidad = float(input(" ingrese laCantidad sin IVA: "))  # indica al usuario quie ingrese la cantidad sin iva

# Pide el  IVA o usa el 21% 
porcentaje = input("IVA  ")
t = float(porcentaje) if porcentaje else 21  # Usa 21 si no se proporciona

# Calcula y muestra el total
total = calcular_factura(cantidad, t)
print("El total de la factura es:", round(total, 2))  # Muestra el total