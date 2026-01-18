#Validar credenciales

print("======= Validar Credenciales =======")

try:
    usuario = input("Digite su usuario: ")
    password = int(input("Digite la contraseña: "))
    
    usuario_correcto = "nestor"
    password_correcto = "1234"
    
    usuario_final = usuario.lower().strip().replace(" ","_")
