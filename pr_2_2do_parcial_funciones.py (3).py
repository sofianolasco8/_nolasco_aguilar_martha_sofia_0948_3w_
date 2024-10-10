print(" ")
print("_nolasco_aguilar_martha_sofia_0948_3W")
def my_function(cantidad_sin, porcentaje_con=21): #definir funciones 
    iva = cantidad_sin * (porcentaje_con / 100) 
    total_con_iva = cantidad_sin + iva
    return total_con_iva

if __name__ == "__main__":
    try:
        cantidad_sin= float(input("ingresa la cantidad sin iva "))
        porcentaje_con_input = input("ingresa el porcentaje de iva ")
        
        # Verificar si el usuario ingresó un porcentaje de IVA
        if porcentaje_con_input:
            porcentaje_iva = float(porcentaje_con_input)
        else:
            porcentaje_iva = 21  # Valor por defecto
        
        total = my_function(cantidad_sin, porcentaje_iva)
        print(f"El total de la factura es  {total:.2f}")
    except ValueError:
        print("ingresa un numero valido")
