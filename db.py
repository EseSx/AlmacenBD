import sqlite3

Alamacen.db = sqlite3.connect("almacen.db")
contraseñasBD = sqlite3.connect("contraseñas.db")

cursor = Alamacen.cursor()
cursorContraseñas = contraseñasBD.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS venta (id INTEGER PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS proveedor (id INTEGER PRIMARY KEY)")