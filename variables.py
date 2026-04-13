#condicionales 

print("hola ingrese la nota del estudiante")
nota = int(input())
if nota >= 7:
    print("aprobado")
else:
    print("reprobado")

#condicionales multiples

print("ingrese el dia de la semana")
dia = input()
match dia:
    case "lunes":
        print("es lunes")
    case "martes":
        print("es martes")
    case _:
        print("otro dia")