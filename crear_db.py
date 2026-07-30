import sqlite3

conexion = sqlite3.connect("lawm.db")

with open("schema.sql", "r", encoding="utf-8") as archivo:
    conexion.executescript(archivo.read())

conexion.commit()
conexion.close()

print("Base de datos creada correctamente")