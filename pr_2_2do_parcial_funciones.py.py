print(" ")
print("Nolasco_aguilar_martha_sofia_0948_3W ")
print(" ")
def saludo():#se crea la funcion
    
    while True:  # indica que se repetirá indefinidamente
        print("Hey amigos!")  # muestra  el saludo
        
        # Pregunta al usuario  si quiere ver el saludo nuevamente
        respuesta = input("¿Quieres ver el saludo de nuevo?  ".strip().lower())
        
        # Si el usuario escribe 'no' se termina 
        if respuesta =='no' :
            print("fin")  # Mensaje de despedida
            break  


saludo()
