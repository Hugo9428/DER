import sqlite3

#conexion
try:
    conexion = sqlite3.connect("DBPython/TablasSQLite")
except Exception as ex:
    print(ex)
#conexion  = sqlite3.connect("TablaSQLite.db")

#cursor
cursor = conexion.cursor()

#crear tablas
cursor.execute("CREATE TABLE IF NOT EXISTS Categoria (ID INTEGER PRIMARY KEY NOT NULL, Nombre TEXT);")
conexion.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Producto (ID INTEGER PRIMARY KEY NOT NULL, Nombre TEXT, Cantidad INTEGER, Precio_unitario INTEGER, Sucursal_ID INTEGER, Categoria_ID INTEGER);")
conexion.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Stock (ID INTEGER PRIMARY KEY NOT NULL, Producto_ID INTEGER, Sucursal_ID INTEGER,  Cantidad INTEGER, UNIQUE (Sucursal_ID, Producto_ID));")
conexion.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Sucursal (ID INTEGER PRIMARY KEY NOT NULL, Nombre TEXT, Direccion TEXT,  Telefono TEXT);")
conexion.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Ordenes (ID INTEGER PRIMARY KEY NOT NULL, Cliente_ID INTEGER, Sucursal_ID INTEGER, Fecha DATE, Total INTEGER);")
conexion.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Cliente (ID INTEGER PRIMARY KEY NOT NULL, Nombre TEXT, Telefono TEXT);")
conexion.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS Item (ID INTEGER PRIMARY KEY NOT NULL, Orden_ID INTEGER, Producto_ID INTEGER, Cantidad INTEGER, Precio INTEGER);")
conexion.commit()


informacion = cursor.fetchall()
for info in informacion:
    print(info)

#guardar cambios
conexion.commit()

#cerrar 
conexion.close()