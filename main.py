# Estilos añadidos
subrayado = "\033[4m"
negrita = "\033[1m"
verde = "\033[32m"
magenta = "\033[35m"
rojo = "\033[31m"
azul = "\033[34m"
amarillo = "\033[33m"
cyanF = "\033[46m"
final = "\033[0m"

import sqlite3

contraseñasbd = sqlite3.connect("contraseñas.db")
cursor = contraseñasbd.cursor()

print(f"{subrayado}{negrita}Bienvenido al programa de 'Sistema de Organizacion y Registro de Almacenes'{final}\n")

while True:
    pregunta1 = input(f"Que accion desea realizar ({rojo}I{final}ngresar datos, {rojo}M{final}odificar datos, {rojo}E{final}liminar datos, {rojo}V{final}er datos y {rojo}S{final}istema de ventas): \n").lower()

    if (pregunta1[0] == "i"):
        pass
    elif (pregunta1[0] == "m"):
        pass
    elif (pregunta1[0] == "e"):
        pass
    elif (pregunta1[0] == "v"):
        pass
    elif (pregunta1[0] == "s"):
        pass
    else:
        print(f"El comando ingresado no a sido reconocido.\nPruebe con uno de los siguientes comandos I <- Para ingresar datos | M <- Para modificar datos existentes |")