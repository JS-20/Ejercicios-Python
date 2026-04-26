# while
#comidas = ["pizza", "hamburguesa", "tacos", "sushi", "pasta"]
#i = 0
#while i < len(comidas):
#    print(comidas[i])
#    i += 1  

#for
#palabra= "Commemoración"
#for letra in palabra:
#    match letra:
#        case "a" | "e" | "i" | "o" | "u":
#             print(f"{letra} es una vocal")
#        case _:
#                print(f"{letra} es una consonante")


# escribir un programa que guarde en variables el monto del ingreso de cada uno de los
# 6 meses del año, luego calcular y guardar en otra variable el promedio de esos 
# valores. Por ultimo, mostrar una leyenda que diga "el ingreso promedio en el semestre es de
# $X" donde X es el valor del promedio calculado.

print("ingrese el monto del ingreso del mes 1")
mes1 = float(input())
print("ingrese el monto del ingreso del mes 2")
mes2 = float(input())
print("ingrese el monto del ingreso del mes 3")
mes3 = float(input())
print("ingrese el monto del ingreso del mes 4")
mes4 = float(input())
print("ingrese el monto del ingreso del mes 5")     
mes5 = float(input())
print("ingrese el monto del ingreso del mes 6")
mes6 = float(input())       
promedio = (mes1 + mes2 + mes3 + mes4 + mes5 + mes6) / 6
print(f"el ingreso promedio en el semestre es de ${promedio}")

