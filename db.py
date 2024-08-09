import sqlite3

Almacendb = sqlite3.connect("almacen.db")
contraseñasBD = sqlite3.connect("contraseñas.db")

cursor = Almacendb.cursor()
cursorContraseñas = contraseñasBD.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS venta (id INTEGER PRIMARY KEY, dia, cantidadTot, precioTot, id_venta, id_producto, FOREIGN KEY (id_producto) REFERENCES productos (id)")
cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, fechaEnt, vencimiento, precioVen, precioXPro, id_proveedor, FOREIGN KEY (id_proveedor) REFERENCES proveedor (id))")
cursor.execute("CREATE TABLE IF NOT EXISTS proveedor (id INTEGER PRIMARY KEY, nombre, productoVen, fechaDeCom, precioCom, nombrePro)")

def agregar():
    pass

def borrar():
    pass

def actualizar():
    pass

# Modificar
Almacendb.commit()