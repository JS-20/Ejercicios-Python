import os
os.system("cls")

#cadena = "hola"
#for letra in range(len(cadena)):
#    print(cadena[letra])

def contar_vocales(cadena):
    contador = 0
    for vocal in cadena:
        if vocal in "aeiouAEIOU":
            contador += 1
    return contador

palabra = input("Ingrese una palabra: ")
vocales = contar_vocales(palabra)
print(f"La palabra '{palabra}' tiene {vocales} vocales.")

for vocal in palabra:
    if vocal in "aeiouAEIOU":
        print(f"{vocal} es una vocal")
   

