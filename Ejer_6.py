#Categorias de Edad

try: 
    Edad = int(input("Digita tu edad: "))

    if Edad < 0 :
        print("Edad no Valida")
    elif Edad < 13:
        print("Eres un Niño")
    elif Edad < 18:
        print("Eres un Adolecente")
    elif Edad < 65:
        print("Eres un Adulto")
    else:
        print("Eres un Adulto Mayor")
        
except ValueError:
    print("Error: Debes ingresar un numero entero")