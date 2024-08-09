# Zona de estilos añadidos
subrayado = "\033[4m"
negrita = "\033[1m"
verde = "\033[32m"
magenta = "\033[35m"
rojo = "\033[31m"
azul = "\033[34m"
amarillo = "\033[33m"
cyanF = "\033[46m"
final = "\033[0m"

# Zona de imports
import sqlite3
from productos import Productos
from proveedor import Proveedor
import db

# Zona de BD
contraseñasbd = sqlite3.connect("../contraseñas.db")
cursor = contraseñasbd.cursor()

# Zona main
print(f"{subrayado}{negrita}Bienvenido al programa de 'Sistema de Organizacion y Registro de Almacenes'{final}\n")

while True:
    pregunta1 = input(f"Que accion desea realizar ({rojo}I{final}ngresar datos, {rojo}M{final}odificar datos, {rojo}E{final}liminar datos, {rojo}V{final}er datos y {rojo}S{final}istema de ventas): \n").lower()

    if (pregunta1[0] == "i"):
        listacontraseñas = cursor.execute("SELECT * FROM Contraseñas")
        contraseña = input("Ingrese contraseña de administrador: ")

        for i in listacontraseñas:
            if contraseña.lower() == i[1]:
                nombre = input("Ingrese el nombre del proveedor: ")
                productoVen = int(input("Ingrese la cantidad de productos ingresados: "))
                fechaDeCom = input("Ingrese la fecha de ingreso del producto (DD/MM/AA): ")
                cantidadCom = int(input("Ingrese el precio de compra del producto: "))
                nombrePro = input("Ingrese el nombre del producto: ")

                proovedorIng = Proveedor(nombre, productoVen, fechaDeCom, cantidadCom, nombrePro)
                
                vencimiento = input("Ingrese la fecha de vencimiento de los productos ingresados (DD/MM/AA): ")
                precioVen = int(input("Ingrese precio de venta de los productos: "))
                precioXPro = int(input("Ingrese el precio individual de los productos: "))

                productoIng = Productos(vencimiento, precioVen, precioXPro)

                db.agregar(proovedorIng, productoIng)

    elif (pregunta1[0] == "m"):
        pass
    elif (pregunta1[0] == "e"):
        pass
    elif (pregunta1[0] == "v"):
        pass
    elif (pregunta1[0] == "s"):
        pass
    else:
        print(f"El comando ingresado no a sido reconocido.\nPruebe con uno de los siguientes comandos I <- Para ingresar datos | M <- Para modificar datos existentes | E <- Para eliminar datos | V <- para ver datos | S <- Para acceder al sistema de ventas")