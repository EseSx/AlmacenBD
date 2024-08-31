import sqlite3

Almacendb = sqlite3.connect("almacen.db")
contraseñasBD = sqlite3.connect("contraseñas.db")

cursor = Almacendb.cursor()
cursorContraseñas = contraseñasBD.cursor()  # Creo los cursores

cursor.execute(
    "CREATE TABLE IF NOT EXISTS venta (id INTEGER PRIMARY KEY, dia, cantidadTot, precioTot, numeroVenta, id_producto, FOREIGN KEY (id_producto) REFERENCES productos (id))"
)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, vencimiento, precioVen, precioXPro, id_proveedor, FOREIGN KEY (id_proveedor) REFERENCES proveedor (id))"
)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS proveedor (id INTEGER PRIMARY KEY, nombre, productoVen, fechaDeCom, cantidadCom, nombrePro)"
)  # Creo las tablas y sus campos


def agregar(proveedor, producto):

    cursor.execute("SELECT MAX(id) FROM proveedor")
    listaProveedor = cursor.fetchone()
    if listaProveedor[0] == None:
        contador = 1
    else:
        contador = listaProveedor[0] + 1  # Creo un contador para conectar las id

    cursor.execute(
        "INSERT INTO proveedor (nombre, productoVen, fechaDeCom, cantidadCom, nombrePro) values (?, ?, ?, ?, ?)",
        (
            proveedor.nombre,
            proveedor.productoVen,
            proveedor.fechaDeCom,
            proveedor.cantidadCom,
            proveedor.nombrePro,
        ),
    )

    cursor.execute(
        "INSERT INTO productos (vencimiento, precioVen, precioXPro, id_proveedor) values (?, ?, ?, ?)",
        (producto.vencimiento, producto.precioVenta, producto.precioXPro, contador),
    )  # Ingreso todos los valores recibidos a sus respectivos campos y tablas

    Almacendb.commit()  # Confirmo los cambios


def borrar(PPOV):
    confirmacion = True
    while confirmacion == True:  # Creo un bucle para borrar datos de forma infinita
        if PPOV[0] == "p" and PPOV[3] == "v":
            listaProveedor = cursor.execute("SELECT * FROM proveedor")
            for i in listaProveedor:
                print(
                    f"Columna nº{i[0]}: \n nombre: {i[1]} \n productoVen: {i[2]} \n fechaDeCom: {i[3]} \n cantidadCom: {i[4]} \n nombrePro: {i[5]}"
                )  # Imprimo las opciones

            columnaEliminar = input(
                "Cual de las columnas presentadas anteriormente desea eliminar? \n"
            )  # consulta la columna a eliminar
            cursor.execute(f"DELETE FROM proveedor WHERE id = {columnaEliminar}")

            Almacendb.commit()  # Confirmo los cambios

        # Repito el proceso con el resto de tablas
        elif PPOV[0] == "p" and PPOV[3] == "d":
            listaProductos = cursor.execute(
                "SELECT productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM productos INNER JOIN proveedor ON productos.id_proveedor = proveedor.id"
            )
            for i in listaProductos:
                print(
                    f"Columna nº{i[0]}: \n vencimiento: {i[1]} \n precioVen: {i[2]} \n precioXPro: {i[3]}"
                )

            columnaEliminar = input(
                "Cual de las columnas presentadas anteriormente desea eliminar? \n"
            )
            cursor.execute(f"DELETE FROM productos WHERE id = {columnaEliminar}")

            Almacendb.commit()

        elif PPOV[0] == "v":
            listaVenta = cursor.execute(
                "SELECT venta.dia, venta.cantidadTot, venta.precioTot, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM venta INNER JOIN productos ON venta.id_producto = productos.id INNER JOIN proveedor ON productos.id_proveedor = proveedor.id"
            )
            for i in listaVenta:
                print(
                    f"Columna nº{i[0]}: \n dia: {i[1]} \n cantidadTot: {i[2]} \n precioTot: {i[3]}"
                )

            campoModificar = input(
                "Cual de los datos presentados anteriormente desea modificar? \n"
            )
            cambio = input("Ingrese el valor modificado: ")
            columnaModificar = input(
                "Cual de las columnas presentadas anteriormente desea modificar? \n"
            )

            cursor.execute(
                f"UPDATE venta SET {campoModificar} = {cambio} WHERE id = {columnaModificar}"
            )

            Almacendb.commit()

    confirmacion = input("Desea modificar otro valor? \n").lower()

    if confirmacion[0] == "s":
        confirmacion = True
    else:
        confirmacion = False  # Confirmo si se siguen eliminando valores


def actualizar(PPOV):
    confirmacion = True
    while (
        confirmacion == True
    ):  # Creo un bucle para modificar valores de manera infinita
        if PPOV[0] == "p" and PPOV[3] == "v":
            listaProveedor = cursor.execute("SELECT * FROM proveedor")
            for i in listaProveedor:
                print(
                    f"Columna nº{i[0]}: \n nombre: {i[1]} \n productoVen: {i[2]} \n fechaDeCom: {i[3]} \n cantidadCom: {i[4]} \n nombrePro: {i[5]}"
                )  # Muestro todas las opciones

            campoModificar = input(
                "Cual de los datos presentados anteriormente desea modificar? \n"
            )
            cambio = input("Ingrese el valor modificado: ")
            columnaModificar = input(
                "Cual de las columnas presentadas anteriormente desea modificar? \n"
            )  # Solicito que campo se quiere modificar, cual es el nuevo valor y en que columna esta presente

            cursor.execute(
                f"UPDATE proveedor SET {campoModificar} = {cambio} WHERE id = {columnaModificar}"
            )

            Almacendb.commit()  # Guardo los cambios

        # Repito el proceso con el resto de tablas
        elif PPOV[0] == "p" and PPOV[3] == "d":
            listaProductos = cursor.execute(
                "SELECT productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM productos INNER JOIN proveedor ON productos.id_proveedor = proveedor.id"
            )
            for i in listaProductos:
                print(
                    f"Columna nº{i[0]}: \n vencimiento: {i[1]} \n precioVen: {i[2]} \n precioXPro: {i[3]}"
                )

            campoModificar = input(
                "Cual de los datos presentados anteriormente desea modificar? \n"
            )
            cambio = input("Ingrese el valor modificado: ")
            columnaModificar = input(
                "Cual de las columnas presentadas anteriormente desea modificar? \n"
            )

            cursor.execute(
                f"UPDATE productos SET {campoModificar} = {cambio} WHERE id = {columnaModificar}"
            )

            Almacendb.commit()

        elif PPOV[0] == "v":
            listaVenta = cursor.execute(
                "SELECT venta.dia, venta.cantidadTot, venta.precioTot, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM venta INNER JOIN productos ON venta.id_producto = productos.id INNER JOIN proveedor ON productos.id_proveedor = proveedor.id"
            )
            for i in listaVenta:
                print(
                    f"Columna nº{i[0]}: \n dia: {i[1]} \n cantidadTot: {i[2]} \n precioTot: {i[3]}"
                )

            campoModificar = input(
                "Cual de los datos presentados anteriormente desea modificar? \n"
            )
            cambio = input("Ingrese el valor modificado: ")
            columnaModificar = input(
                "Cual de las columnas presentadas anteriormente desea modificar? \n"
            )

            cursor.execute(
                f"UPDATE venta SET {campoModificar} = {cambio} WHERE id = {columnaModificar}"
            )

            Almacendb.commit()

    confirmacion = input("Desea modificar otro valor? \n").lower()

    if confirmacion[0] == "s":
        confirmacion = True
    else:
        confirmacion = False  # Confirmo si se siguen modificando valores


def venta(venta, producto):
    cursor.execute(
        "INSERT INTO venta (dia, cantidadTot, precioTot, numeroVenta, id_producto) values (?, ?, ?, ?, ?)",
        (
            venta.dia,
            venta.cantidadTotal,
            venta.precioTotal,
            venta.numeroVenta,
            producto,
        ),
    )

    Almacendb.commit()  # Inserto los datos y guardo los cambios


# Modificar
Almacendb.commit()
