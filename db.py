import sqlite3

Almacendb = sqlite3.connect("almacen.db")
contraseñasBD = sqlite3.connect("contraseñas.db")

cursor = Almacendb.cursor()
cursorContraseñas = contraseñasBD.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS venta (id INTEGER PRIMARY KEY, dia, cantidadTot, precioTot, id_venta, id_producto, FOREIGN KEY (id_producto) REFERENCES productos (id))")
cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, vencimiento, precioVen, precioXPro, id_proveedor, FOREIGN KEY (id_proveedor) REFERENCES proveedor (id))")
cursor.execute("CREATE TABLE IF NOT EXISTS proveedor (id INTEGER PRIMARY KEY, nombre, productoVen, fechaDeCom, cantidadCom, nombrePro)")

contador = 0

def agregar(proveedor, producto):

    listaProveedores = cursor.execute("SELECT proveedor.id FROM proveedor")
    global contador
    for i in listaProveedores:
        contador = (i[0] + 1)

    cursor.execute("INSERT INTO proveedor (nombre, productoVen, fechaDeCom, cantidadCom, nombrePro) values (?, ?, ?, ?, ?)", (proveedor.nombre, proveedor.productoVen, proveedor.fechaDeCom, proveedor.cantidadCom, proveedor.nombrePro))

    cursor.execute("INSERT INTO productos (vencimiento, precioVen, precioXPro, id_proveedor) values (?, ?, ?, ?)", (producto.vencimiento, producto.precioVenta, producto.precioXPro, contador))

    Almacendb.commit()

def borrar():
    pass

def actualizar(PPOV):
    if (PPOV[0] == "p" and PPOV[3] == "v"):
        listaProveedor = cursor.execute("SELECT * FROM proveedor")
        for i in listaProveedor:
            print(f"Columna nº{i[0]}: \n nombre: {i[1]} \n productoVen: {i[2]} \n fechaDeCom: {i[3]} \n cantidadCom: {i[4]} \n nombrePro: {i[5]}")
        
        campoModificar = input("Cual de los datos presentados anteriormente desea modificar? \n")
        cambio = input("Ingrese el valor modificado: ")
        columnaModificar = input("Cual de las columnas presentadas anteriormente desea modificar? \n")

        cursor.execute(f"UPDATE proveedor SET {campoModificar} = {cambio} WHERE id = {columnaModificar}")

        Almacendb.commit()
        Almacendb.close()
    
    elif (PPOV[0] == "p" and PPOV[3] == "d"):
        listaProductos = cursor.execute("SELECT productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM productos INNER JOIN proveedor ON productos.id_proveedor = proveedor.id")
        for i in listaProductos:
            print(f"Columna nº{i[0]}: \n vencimiento: {i[1]} \n precioVen: {i[2]} \n precioXPro: {i[3]}")

        campoModificar = input("Cual de los datos presentados anteriormente desea modificar? \n")
        cambio = input("Ingrese el valor modificado: ")
        columnaModificar = input("Cual de las columnas presentadas anteriormente desea modificar? \n")

        cursor.execute(f"UPDATE productos SET {campoModificar} = {cambio} WHERE id = {columnaModificar}")

        Almacendb.commit()
        Almacendb.close()

    elif (PPOV[0] == "v"):
        listaVenta = cursor.execute("SELECT venta.dia, venta.cantidadTot, venta.precioTot, productos.vencimiento, productos.precioVen, productos.precioXPro, proveedor.nombre, proveedor.productoVen, proveedor.cantidadCom, proveedor.nombrePro FROM venta INNER JOIN productos ON venta.id_producto = productos.id INNER JOIN proveedor ON productos.id_proveedor = proveedor.id")
        for i in listaVenta:
            print(f"Columna nº{i[0]}: \n dia: {i[1]} \n cantidadTot: {i[2]} \n precioTot: {i[3]}")

        campoModificar = input("Cual de los datos presentados anteriormente desea modificar? \n")
        cambio = input("Ingrese el valor modificado: ")
        columnaModificar = input("Cual de las columnas presentadas anteriormente desea modificar? \n")

        cursor.execute(f"UPDATE venta SET {campoModificar} = {cambio} WHERE id = {columnaModificar}")

        Almacendb.commit()
        Almacendb.close()

# Modificar
Almacendb.commit()