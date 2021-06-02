import sqlite3

conexion = sqlite3.connect('base.db')
cursor = conexion.cursor()

#conexion.execute("CREATE TABLE clientes (dni integer, apellido varchar(100), nombre varchar(100))")

##cursor.execute("INSERT INTO clientes VALUES(35000,'Martin', 'Pared')")
##cursor.execute("INSERT INTO clientes VALUES(350001,'Jose', 'Baez')")

##cursor.execute("SELECT * FROM clientes")
##result = cursor.fetchone()
##print(result)

##result = cursor.fetchone()
##print(result)
##print("DNI", result[0])
##print("Nombre: ", result[1])
##print("Apellido: ", result[2])

##clientesAlta = [
##        (35001377, 'Martin 1', 'Pared 1'),
##        (35001378, 'Jose 1', 'Baez 1'),
##    ]
##cursor.executemany("INSERT INTO clientes VALUES(?,?,?)",clientesAlta)
cursor.execute("SELECT * FROM clientes")
results = cursor.fetchall()
##print(results)
#for result in results:
#    print("DNI", result[0])
#    print("Nombre: ", result[1])
#   print("Apellido: ", result[2])

##cursor.execute("""
##        CREATE TABLE proveedores
##        (
##        dni varcahar(8) primary key,
##       apellido varchar(100),
##       nombre varchar(100)
##       )
##""")

##proveedoresAlta = [
####        ('35001377', 'Martin', 'Pared'),
#       ('35001378', 'Jose', 'Baez'),
##    ]
##cursor.executemany("INSERT INTO proveedores VALUES(?,?,?)",proveedoresAlta)

#cursor.execute("""
#        CREATE TABLE socios
#        (
#        id integer primary key autoincrement,
#      apellido varchar(100),
#       nombre varchar(100)
#       )
#""")

#sociosAlta = [
#    ('Martin', 'Pared'),
#    ('Jose', 'Baez'),
#    ]
#cursor.executemany("INSERT INTO socios VALUES(null,?,?)",sociosAlta)


cursor.execute("""
        CREATE TABLE test
        (
        id integer primary key autoincrement,
        dni integer unique,
        apellido varchar(100),
        nombre varchar(100)
       )
""")
conexion.commit()
conexion.close()
