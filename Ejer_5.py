#Sistema de Calificaciones

nota = input("Digita la nota: ")

if nota >= 0 and nota < 59:
    print("Tu calificacion es F")
elif nota >= 60 and nota < 69:
    print("Tu calificacion es D")
elif nota >= 70 and nota < 79:
    print("Tu calificacion es C")
elif nota >= 80 and nota < 89:
    print("Tu calificacion es B")
else:
    print("Tu calificacion es A")