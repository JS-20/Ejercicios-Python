#condicionales 

print("hola ingrese la nota del estudiante")
nota = int(input())
if nota >= 7:
    print("aprobado")
else:
    print("reprobado")

#condicionales multiples

print("ingrese el numero de dia de la semana")
dia = int(input())
match dia:
    case 1:
        print("es lunes")
    case 2:
        print("es martes")
    case 3:
        print("miercoles")
    case 4:
        print("jueves") 
    case 5:
        print("viernes")    
    case 6:
        print("sabado")             
    case 7:
        print("domingo")      

#              
