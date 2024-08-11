import sqlite3

Almacendb = sqlite3.connect("almacen.db")
contraseñasBD = sqlite3.connect("contraseñas.db")

cursor = Almacendb.cursor()
cursorContraseñas = contraseñasBD.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS venta (id INTEGER PRIMARY KEY, dia, cantidadTot, precioTot, id_venta, id_producto, FOREIGN KEY (id_producto) REFERENCES productos (id))")
cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, vencimiento, precioVen, precioXPro, id_proveedor, FOREIGN KEY (id_proveedor) REFERENCES proveedor (id))")
cursor.execute("CREATE TABLE IF NOT EXISTS proveedor (id INTEGER PRIMARY KEY, nombre, productoVen, fechaDeCom, cantidadCom, nombrePro)")

def agregar(proveedor, producto):
    cursor.execute("INSERT INTO proveedor (nombre, productoVen, fechaDeCom, cantidadCom, nombrePro) values (?, ?, ?, ?, ?)", (proveedor.nombre, proveedor.productoVen, proveedor.fechaDeCom, proveedor.cantidadCom, proveedor.nombrePro))
    cursor.execute("INSERT INTO productos (vencimiento, precioVen, precioXPro) values (?, ?, ?)", (producto.vencimiento, producto.precioVenta, producto.precioXPro))

    Almacendb.commit()

def borrar():
    pass

def actualizar():
    pass

# Modificar
Almacendb.commit()