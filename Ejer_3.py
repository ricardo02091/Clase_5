#Ejercicio de edad

nombre = input("¿Como te llamas? ")
edad = int(input("¿Cuantos años tienes? "))

if edad >= 18:
    print(f"Hola {nombre}, eres mayor de edad, Acceso permitido")
    
else:
    print(f"Lo lamento {nombre}, eres menor de edad, Acceso denegado")