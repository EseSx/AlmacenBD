# Zona de estilos añadidos
subrayado = "\033[4m"
negrita = "\033[1m"
rojo = "\033[31m"
final = "\033[0m"

# Zona de imports
import sqlite3
from productos import Productos
from proveedor import Proveedor
from venta import venta
import db

# Zona de BD
contraseñasbd = sqlite3.connect("contraseñas.db")
cursor = contraseñasbd.cursor()

# Zona main
print(
    f"{subrayado}{negrita}Bienvenido al programa de 'Ventas y Organizacion para Almacenes'{final}\n"
)

print(
    f"{subrayado}{negrita}{rojo}ADVERTENCIAS:{final}\n {negrita}·{final}El programa utiliza comandos de texto para acceder a las distintas funciones, en los ejemplos saldran escritas en rojo las letras minimas que deben ser ingresadas para acceder a estas mismas funciones. {subrayado}Cosas a tener en cuenta{final}:\n  {negrita}1.{final}Los comandos pueden ser escritos en minusculas o mayusculas.\n  {negrita}2.{final}No utilice signos de puntuacion dentro del rango de las letras rojas.\n ·Todos los valores numericos ingresados a la Base de Datos seran guardados como 'float', 'valores con coma', 'con punto' o 'con decimales', esto para evitar errores y crasheos en el codigo. {subrayado}Cosas a tener en cuenta{final}:\n  {negrita}1.{final}Tome en el programa seran usados como 'float' por lo tanto evite ingresar numeros, como por ejemplo el 1000 de las siguientes formas, '1.000'/'1,000'/'1000,00', se le recomienda ingresarlo de la siguiente forma en caso de ser un numero entero '1000', y en caso de ser un numero con decimales se recomienda ingresarlo de esta forma '1000.05'.\n"
)

# Bucle infinito
while True:

    # Peticiones extra del profe
    print(
        f"{subrayado}Ultimos productos en stock, con cantidad menor a 10 unidades:{final}"
    )
    db.cursor.execute("SELECT id FROM proveedor WHERE cantidadCom < 10")
    ultimosProductos = db.cursor.fetchall()
    for dato in ultimosProductos:
        id_producto = dato[0]
        fila = db.cursor.execute(
            "SELECT productos.id, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM productos INNER JOIN proveedor ON productos.id_proveedor = proveedor.id WHERE proveedor.id = ?",
            (id_producto,),
        )
        fila = db.cursor.fetchall()
        if fila:
            for i in fila:
                print(
                    f"\nColumna nº{i[0]}: \n Vencimiento: {i[1]} \n Precio de venta: {i[2]} \n Precio por producto: {i[3]} \n Proveedor nombre: {i[4]} \n Precio de venta del producto del proveedor: {i[5]} \n Cantidad del producto comprado: {i[6]} \n Nombre de producto: {i[7]}\n"
                )

    print(f"{subrayado}Ultimos 5 productos vendidos:{final}")
    db.cursor.execute("SELECT id_producto FROM venta ORDER BY numeroVenta ASC LIMIT 5")
    ultimosVendidos = db.cursor.fetchall()
    for dato in ultimosVendidos:
        id_producto = dato[0]
        fila = db.cursor.execute(
            "SELECT productos.id, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM productos INNER JOIN proveedor ON productos.id_proveedor = proveedor.id WHERE productos.id = ?",
            (id_producto,),
        )
        fila = db.cursor.fetchall()
        if fila:
            for i in fila:
                print(
                    f"\nColumna nº{i[0]}: \n Vencimiento: {i[1]} \n Precio de venta: {i[2]} \n Precio por producto: {i[3]} \n Proveedor nombre: {i[4]} \n Precio de venta del producto del proveedor: {i[5]} \n Cantidad del producto comprado: {i[6]} \n Nombre de producto: {i[7]}\n"
                )

    print(f"{subrayado}Valor total del inventario:{final}")
    db.cursor.execute("SELECT precioXPro FROM productos")
    valorTot = db.cursor.fetchall()
    resValor = 0
    for dato in valorTot:
        resValor += dato[0]
    print(f"El precio total del inventario es ${resValor}")

    # Funcionamiento principal
    pregunta1 = input(
        f"Que accion desea realizar ({rojo}I{final}ngresar datos, {rojo}M{final}odificar datos, {rojo}E{final}liminar datos, {rojo}V{final}er datos y {rojo}S{final}istema de ventas): \n"
    ).lower()  # Consulto la funcion a realizar

    # Sistema para ingresar datos
    if pregunta1[0] == "i":
        listacontraseñas = cursor.execute("SELECT * FROM Contraseñas")
        contraseña = input(
            "Ingrese contraseña de administrador: "
        )  # Consulto y evaluo una contraseña

        for i in listacontraseñas:
            if contraseña.lower() == i[1]:
                nombre = input("Ingrese el nombre del proveedor: ").lower()
                productoVen = float(
                    input("Ingrese el precio por el que compramos el producto: ")
                )
                fechaDeCom = input(
                    "Ingrese la fecha de ingreso del producto (DD/MM/AA): "
                ).lower()
                cantidadCom = float(
                    input("Ingrese la cantidad comprada del producto: ")
                )
                nombrePro = input(
                    "Ingrese el nombre del producto: "
                ).lower()  # Solicito todos los datos del proveedor

                proovedorIng = Proveedor(
                    nombre, productoVen, fechaDeCom, cantidadCom, nombrePro
                )  # Uso POO para organizar la informacion pedida en un nuevo objeto

                vencimiento = input(
                    "Ingrese la fecha de vencimiento de los productos ingresados (DD/MM/AA): "
                ).lower()
                precioVen = float(
                    input("Ingrese precio de venta de los productos por pack o caja: ")
                )
                precioXPro = float(
                    input("Ingrese el precio individual de los productos: ")
                )

                productoIng = Productos(
                    vencimiento, precioVen, precioXPro
                )  # Realizo el mismo procedimiento con el producto

                db.agregar(
                    proovedorIng, productoIng
                )  # Se lo envio al codigo de la base de datos

    # Sistema para modificar datos
    elif pregunta1[0] == "m":
        listacontraseñas = cursor.execute("SELECT * FROM Contraseñas")
        contraseña = input(
            "Ingrese contraseña de administrador: "
        )  # Hago el mismo proceso de las contraseñas

        for i in listacontraseñas:
            if contraseña.lower() == i[1]:
                PPOV = input(
                    f"Que tabla desea modificar {rojo}Prov{final}eedor, {rojo}Prod{final}ucto, {rojo}V{final}enta: "
                ).lower()  # Consulto que tabla se va a modificar

                if PPOV[0] == "p" and PPOV[3] == "v":
                    confirmacion = input(
                        "Esta seguro de que quiere modificar algun dato de la tabla de proveedores?: "
                    ).lower()  # Confirmo la solicitud

                    if confirmacion[0] == "s":
                        db.actualizar(
                            PPOV
                        )  # Mando una señal al codigo de la base de datos

                elif PPOV[0] == "p" and PPOV[3] == "d":
                    confirmacion = input(
                        "Esta seguro de que quiere modificar algun dato de la tabla de productos?: "
                    ).lower()

                    if confirmacion[0] == "s":
                        db.actualizar(PPOV)  # Repito el proceso con los productos

                elif PPOV[0] == "v":
                    confirmacion = input(
                        "Esta seguro de que quiere modificar algun dato de la tabla de venta?: "
                    ).lower()

                    if confirmacion[0] == "s":
                        db.actualizar(PPOV)  # Repito el proceso con la venta

                else:
                    print(
                        f"Ninguno de los comandos ingresados es correcto para modificar proveedor ingrese -> {rojo}PROV{final} | producto ingrese -> {rojo}PROD{final} | venta ingrese -> {rojo}V{final}"
                    )  # Lo que pasa si se equivocan al escribir el comando

    # Sistema para eliminar datos
    elif pregunta1[0] == "e":
        listacontraseñas = cursor.execute("SELECT * FROM Contraseñas")
        contraseña = input(
            "Ingrese contraseña de administrador: "
        )  # Hago devuelta el proceso de la contraseña

        for i in listacontraseñas:
            if contraseña.lower() == i[1]:
                PPOV = input(
                    f"Que tabla desea modificar {rojo}Prov{final}eedor, {rojo}Prod{final}ucto, {rojo}V{final}enta: "
                ).lower()  # Consulto la tabla a modificar

                if PPOV[0] == "p" and PPOV[3] == "v":
                    confirmacion = input(
                        "Esta seguro de que quiere eliminar algun dato de la tabla de proveedores?: "
                    ).lower()  # Confimo la accion

                    if confirmacion[0] == "s":
                        db.borrar(PPOV)  # Mando una señal al codigo de la BD

                # Repito el proceso con la tabla de productos
                elif PPOV[0] == "p" and PPOV[3] == "d":
                    confirmacion = input(
                        "Esta seguro de que quiere eliminar algun dato de la tabla de productos?: "
                    ).lower()

                    if confirmacion[0] == "s":
                        db.borrar(PPOV)

                # Repito el proceso con la tabla de venta
                elif PPOV[0] == "v":
                    confirmacion = input(
                        "Esta seguro de que quiere eliminar algun dato de la tabla de venta?: "
                    ).lower()

                    if confirmacion[0] == "s":
                        db.borrar(PPOV)

                else:
                    print(
                        f"Ninguno de los comandos ingresados es correcto para modificar proveedor ingrese -> {rojo}PROV{final} | producto ingrese -> {rojo}PROD{final} | venta ingrese -> {rojo}V{final}"
                    )

    # Sistema para ver datos
    elif pregunta1[0] == "v":
        PPOV = input(
            f"Que tabla desea ver? ({rojo}Prod{final}uctos, {rojo}Prov{final}eedor o {rojo}V{final}enta)"
        ).lower()  # Consulto que tabla desea visualizar

        if PPOV[0] == "p" and PPOV[3] == "v":
            pregunta = input(
                f"Quiere ver la lista de todos los proveedores o quiere buscar uno en particular? ({rojo}t{final}odo o {rojo}b{final}usqueda): "
            )  # Consulto si ver todo o si buscar un proveedor en particular
            if pregunta.lower()[0] == "t":
                listaProveedor = db.cursor.execute(
                    "SELECT * FROM proveedor"
                )  # Obtengo todo desde proveedores

                for i in listaProveedor:
                    print(
                        f"\nColumna nº{i[0]}: \n Nombre: {i[1]} \n Precio de venta del producto del proveedor: {i[2]} \n Fecha de compra: {i[3]} \n Cantidad del producto comprado: {i[4]} \n Nombre de producto: {i[5]}\n"
                    )  # Imprimo todo lo que obtengo

            elif pregunta.lower()[0] == "b":
                categoria = input(
                    f"Seleccione un categoria ({rojo}N{final}ombre, {rojo}P{final}roductoVen, {rojo}F{final}echaDeCom, {rojo}C{final}antidadCom, {rojo}NombreP{final}ro): "
                )  # Solicito el campo a buscar
                if categoria.lower()[0] == "n":
                    nombre = input(
                        "A seleccionado 'nombre' (Tome en cuenta que debe ser epecifico a la hora de buscar el nombre): "
                    )  # Pido que se ingrese el valor para buscar
                    db.cursor.execute(
                        f"SELECT * FROM proveedor WHERE nombre LIKE '{nombre}%'"
                    )
                    resultados = (
                        db.cursor.fetchall()
                    )  # Recibo y guardo todas las coincidencias
                    if resultados:
                        for dato in resultados:
                            id_proveedor = dato[0]
                            fila = db.cursor.execute(
                                "SELECT * FROM proveedor WHERE id = ?", (id_proveedor,)
                            )
                            fila = (
                                db.cursor.fetchall()
                            )  # Saco todos los datos de las filas con coincidencia

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n Nombre: {i[1]} \n Precio de venta del producto del proveedor: {i[2]} \n Fecha de compra: {i[3]} \n Cantidad del producto comprado: {i[4]} \n Nombre de producto: {i[5]}\n"
                                    )  # Imprimo los datos obtenidos

                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print(
                            "No se encontraron proveedores"
                        )  # Imprimo en caso de no encontrar nada

                # Repito el proceso para el resto de campos
                elif categoria.lower()[0] == "p":
                    productoVen = input(
                        "A seleccionado 'ProductoVen' (Tome en cuenta que debe ser bastante especifico): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM proveedor WHERE productoVen LIKE '{productoVen}'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_proveedor = dato[0]
                            fila = db.cursor.execute(
                                "SELECT * FROM proveedor WHERE id = ?",
                                (id_proveedor,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n Nombre: {i[1]} \n Precio de venta del producto del proveedor: {i[2]} \n Fecha de compra: {i[3]} \n Cantidad del producto comprado: {i[4]} \n Nombre de producto: {i[5]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron proveedores")

                elif categoria.lower()[0] == "f":
                    fechaDeCom = input(
                        "A seleccionado 'FechaDeCom' (Tome en cuenta que debe ser bastante especifico): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM proveedor WHERE fechaDeCom LIKE '{fechaDeCom}'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_proveedor = dato[0]
                            fila = db.cursor.execute(
                                "SELECT * FROM proveedor WHERE id = ?",
                                (id_proveedor,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n Nombre: {i[1]} \n Precio de venta del producto del proveedor: {i[2]} \n Fecha de compra: {i[3]} \n Cantidad del producto comprado: {i[4]} \n Nombre de producto: {i[5]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron proveedores")

                elif categoria.lower()[0] == "c":
                    cantidadCom = input(
                        "A seleccionado 'CantidadCom' (Tome en cuenta que debe ser bastante especifico): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM proveedor WHERE cantidadCom LIKE '{cantidadCom}'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_proveedor = dato[0]
                            fila = db.cursor.execute(
                                "SELECT * FROM proveedor WHERE id = ?",
                                (id_proveedor,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n Nombre: {i[1]} \n Precio de venta del producto del proveedor: {i[2]} \n Fecha de compra: {i[3]} \n Cantidad del producto comprado: {i[4]} \n Nombre de producto: {i[5]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron proveedores")

                elif categoria.lower()[0] == "n" and categoria.lower()[6] == "p":
                    nombrePro = input(
                        "A seleccionado 'NombrePro' (Tome en cuenta que debe ser bastante especifico): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM proveedor WHERE nombrePro LIKE '{nombrePro}'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_proveedor = dato[0]
                            fila = db.cursor.execute(
                                "SELECT * FROM proveedor WHERE id = ?",
                                (id_proveedor,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n Nombre: {i[1]} \n Precio de venta del producto del proveedor: {i[2]} \n Fecha de compra: {i[3]} \n Cantidad del producto comprado: {i[4]} \n Nombre de producto: {i[5]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron proveedores")

            else:
                print("Presione b para buscar o t para mostrar todo")

        # Repito el proceso para el resto de tablas
        elif PPOV[0] == "p" and PPOV[3] == "d":
            pregunta = input(
                f"Quiere ver la lista de todos los productos o quiere buscar uno en particular? ({rojo}t{final}odo o {rojo}b{final}usqueda): "
            )
            if pregunta.lower()[0] == "t":
                listaProductos = db.cursor.execute(
                    "SELECT productos.id, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM productos INNER JOIN proveedor ON productos.id_proveedor = proveedor.id"
                )
                for i in listaProductos:
                    print(
                        f"\nColumna nº{i[0]}: \n Vencimiento: {i[1]} \n Precio de venta: {i[2]} \n Precio por producto: {i[3]} \n Proveedor nombre: {i[4]} \n Precio de venta del producto del proveedor: {i[5]} \n Cantidad del producto comprado: {i[6]} \n Nombre de producto: {i[7]}\n"
                    )

            elif pregunta.lower()[0] == "b":
                categoria = input(
                    f"Seleccione un categoria ({rojo}V{final}encimiento, {rojo}PrecioV{final}en, {rojo}PrecioX{final}Pro): "
                )

                if categoria.lower()[0] == "v":
                    vencimiento = input(
                        "A seleccionado 'Vencimiento' (Tome en cuenta que debe ser epecifico a la hora de buscar la fecha de vencimiento): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM productos WHERE vencimiento LIKE '{vencimiento}%'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_producto = dato[0]
                            fila = db.cursor.execute(
                                "SELECT productos.id, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM productos INNER JOIN proveedor ON productos.id_proveedor = proveedor.id WHERE productos.id = ?",
                                (id_producto,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n Vencimiento: {i[1]} \n Precio de venta: {i[2]} \n Precio por producto: {i[3]} \n Proveedor nombre: {i[4]} \n Precio de venta del producto del proveedor: {i[5]} \n Cantidad del producto comprado: {i[6]} \n Nombre de producto: {i[7]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron productos")

                elif categoria.lower()[0] == "p" and categoria.lower()[6] == "v":
                    precioVen = input(
                        "A seleccionado 'PrecioVen' (Tome en cuenta que debe ser bastante especifico): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM productos WHERE precioVen LIKE '{precioVen}'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_productos = dato[0]
                            fila = db.cursor.execute(
                                "SELECT productos.id, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM productos INNER JOIN proveedor ON productos.id_proveedor = proveedor.id WHERE productos.id = ?",
                                (id_producto,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n Vencimiento: {i[1]} \n Precio de venta: {i[2]} \n Precio por producto: {i[3]} \n Proveedor nombre: {i[4]} \n Precio de venta del producto del proveedor: {i[5]} \n Cantidad del producto comprado: {i[6]} \n Nombre de producto: {i[7]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron productos")

                elif categoria.lower()[0] == "p" and categoria.lower()[6] == "x":
                    precioXPro = input(
                        "A seleccionado 'PrecioXPro' (Tome en cuenta que debe ser bastante especifico): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM productos WHERE precioXPro LIKE '{precioXPro}'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_producto = dato[0]
                            fila = db.cursor.execute(
                                "SELECT productos.id, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM productos INNER JOIN proveedor ON productos.id_proveedor = proveedor.id WHERE productos.id = ?",
                                (id_producto,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n Vencimiento: {i[1]} \n Precio de venta: {i[2]} \n Precio por producto: {i[3]} \n Proveedor nombre: {i[4]} \n Precio de venta del producto del proveedor: {i[5]} \n Cantidad del producto comprado: {i[6]} \n Nombre de producto: {i[7]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron productos")

            else:
                print("Presione b para buscar o t para mostrar todo")

        elif PPOV[0] == "v":
            pregunta = input(
                f"Quiere ver la lista de todas las ventas o quiere buscar uno en particular? ({rojo}t{final}odo o {rojo}b{final}usqueda): "
            )
            if pregunta.lower()[0] == "t":
                listaVentas = db.cursor.execute(
                    "SELECT venta.dia, venta.cantidadTot, venta.precioTot, venta.numeroVenta, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM venta INNER JOIN productos ON venta.id_producto = productos.id INNER JOIN proveedor ON productos.id_proveedor = proveedor.id"
                )
                for i in listaVentas:
                    print(
                        f"\nColumna nº{i[0]}: \n dia: {i[1]} \n Cantidad total del producto vendido: {i[2]} \n Precio total del producto vendido y sus unidades: {i[3]} \n Numero de la venta: {i[4]} \n Nombre del producto vendido: {i[11]} \n Precio individual del producto: {i[6]}\n"
                    )

            elif pregunta.lower()[0] == "b":
                categoria = input(
                    f"Seleccione un categoria ({rojo}D{final}ia, {rojo}C{final}antidadTot, {rojo}P{final}recioTot, {rojo}N{final}umeroVenta): "
                )

                if categoria.lower()[0] == "d":
                    dia = input(
                        "A seleccionado 'Dia' (Tome en cuenta que debe ser epecifico): "
                    )
                    db.cursor.execute(f"SELECT * FROM venta WHERE dia LIKE '{dia}%'")
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_venta = dato[0]
                            fila = db.cursor.execute(
                                "SELECT venta.id, venta.dia, venta.cantidadTot, venta.precioTot, venta.numeroVenta, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM venta INNER JOIN productos ON venta.id_producto = productos.id INNER JOIN proveedor ON productos.id_proveedor = proveedor.id WHERE venta.id = ?",
                                (id_venta,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n dia: {i[1]} \n Cantidad total del producto vendido: {i[2]} \n Precio total del producto vendido y sus unidades: {i[3]} \n Numero de la venta: {i[4]} \n Nombre del producto vendido: {i[11]} \n Precio individual del producto: {i[7]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                if continuar == str or continuar == int:
                                    break

                    else:
                        print("No se encontraron ventas")

                elif categoria.lower()[0] == "c":
                    cantidadTot = input(
                        "A seleccionado 'CantidadTot' (Tome en cuenta que debe ser bastante especifico): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM venta WHERE cantidadTot LIKE '{cantidadTot}'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_venta = dato[0]
                            fila = db.cursor.execute(
                                "SELECT venta.id, venta.dia, venta.cantidadTot, venta.precioTot, venta.numeroVenta, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM venta INNER JOIN productos ON venta.id_producto = productos.id INNER JOIN proveedor ON productos.id_proveedor = proveedor.id WHERE venta.id = ?",
                                (id_venta,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n dia: {i[1]} \n Cantidad total del producto vendido: {i[2]} \n Precio total del producto vendido y sus unidades: {i[3]} \n Numero de la venta: {i[4]} \n Nombre del producto vendido: {i[11]} \n Precio individual del producto: {i[7]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron ventas")

                elif categoria.lower()[0] == "p":
                    precioTot = input(
                        "A seleccionado 'PrecioTot' (Tome en cuenta que debe ser bastante especifico): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM venta WHERE precioTot LIKE '{precioTot}'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_venta = dato[0]
                            fila = db.cursor.execute(
                                "SELECT venta.id, venta.dia, venta.cantidadTot, venta.precioTot, venta.numeroVenta, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM venta INNER JOIN productos ON venta.id_producto = productos.id INNER JOIN proveedor ON productos.id_proveedor = proveedor.id WHERE venta.id = ?",
                                (id_venta,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n dia: {i[1]} \n Cantidad total del producto vendido: {i[2]} \n Precio total del producto vendido y sus unidades: {i[3]} \n Numero de la venta: {i[4]} \n Nombre del producto vendido: {i[11]} \n Precio individual del producto: {i[7]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron ventas")

                elif categoria.lower()[0] == "n":
                    numeroVenta = input(
                        "A seleccionado 'NumeroVenta' (Tome en cuenta que debe ser bastante especifico): "
                    )
                    db.cursor.execute(
                        f"SELECT * FROM venta WHERE numeroVenta LIKE '{numeroVenta}'"
                    )
                    resultados = db.cursor.fetchall()
                    if resultados:
                        for dato in resultados:
                            id_venta = dato[0]
                            fila = db.cursor.execute(
                                "SELECT venta.id, venta.dia, venta.cantidadTot, venta.precioTot, venta.numeroVenta, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM venta INNER JOIN productos ON venta.id_producto = productos.id INNER JOIN proveedor ON productos.id_proveedor = proveedor.id WHERE venta.id = ?",
                                (id_venta,),
                            )
                            fila = db.cursor.fetchall()

                            if fila:
                                for i in fila:
                                    print(
                                        f"\nColumna nº{i[0]}: \n dia: {i[1]} \n Cantidad total del producto vendido: {i[2]} \n Precio total del producto vendido y sus unidades: {i[3]} \n Numero de la venta: {i[4]} \n Nombre del producto vendido: {i[11]} \n Precio individual del producto: {i[7]}\n"
                                    )
                                    continuar = input(f'Si desea continuar pulse cualquier boton: ').lower()

                                    if continuar == str or continuar == int:
                                        continue

                    else:
                        print("No se encontraron ventas")

            else:
                print("Presione b para buscar o t para mostrar todo")

    # Sistema para realizar ventas
    elif pregunta1[0] == "s":
        pagoActual = 0
        db.cursor.execute("SELECT MAX(numeroVenta) FROM venta")
        listaVentas = db.cursor.fetchone()
        if listaVentas[0] == None:
            contador = 1
        else:
            contador = float(listaVentas[0]) + 1  # Genero un numero de venta

        print(f"Se ha iniciado la venta nº{contador}")
        dia = input(
            "Porfavor ingrese el dia de la compra (DD/MM/AA): "
        )  # Solicito una fecha

        cuestion = "s"
        while (
            cuestion[0] == "s"
        ):  # Repito de forma necesaria este codigo bajo una cuestion

            producto = input("Porfavor ingrese el producto comprado: ").lower()
            cantidad = int(
                input("Porfavor ingrese la cantidad de producto que se compro: ")
            )  # Solicito que se ingresen los valores necesarios

            conseguirDesdeProveedor = db.cursor.execute(
                f"SELECT cantidadCom, id FROM proveedor WHERE nombrePro LIKE '{producto}'"
            )
            resProveedor = db.cursor.fetchone()
            if resProveedor:
                cantidadActualizada = float(resProveedor[0]) - int(cantidad)

                db.cursor.execute(
                    f"UPDATE proveedor SET cantidadCom = {cantidadActualizada} WHERE id = {resProveedor[1]}"
                )  # Solicito la cantidad de unidades que hay de un producto y les descuento la cantidad que compraron

                conseguirDesdeProductos = db.cursor.execute(
                    f"SELECT precioXPro, id FROM productos WHERE id_proveedor LIKE '{resProveedor[1]}'"
                )
                resProductos = db.cursor.fetchone()

                pagoActual += (resProductos[0]) * int(cantidad)
                print(
                    f"PRECIO TOTAL DE LA COMPRA: ${pagoActual}"
                )  # Consigo el precio, lo calculo y entrego el precio total de la compra

                ventaing = venta(
                    dia, cantidad, pagoActual, contador
                )  # Uso POO para organizar todos los datos obtenidos

                db.venta(ventaing, resProductos[1])  # Le envio los datos al codigo de la BD

                db.Almacendb.commit()  # Confirmo los cambios hechos en el main
            else:
                continue

            cuestion = input(
                f"Desea ingresar otro producto ({rojo}S{final}i, {rojo}N{final}o)"
            ).lower()  # Solicito si la compra continua

    else:
        print(
            f"El comando ingresado no a sido reconocido.\nPruebe con uno de los siguientes comandos I <- Para ingresar datos | M <- Para modificar datos existentes | E <- Para eliminar datos | V <- para ver datos | S <- Para acceder al sistema de ventas"
        )  # Imprimo esto en caso de que no se escriba ningun comando
