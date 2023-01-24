import mysql.connector


try:
    conexion = mysql.connector.connect(user="root", password="", host="localhost", 
    database="crudpython")
except mysql.connector.Error as err:
    print("Ha ocurrido un error al establecer la conexión: {}".format(err))

