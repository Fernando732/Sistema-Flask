from flask import Flask, request, jsonify, send_file
import conexion


app = Flask(__name__)

@app.route("/api/user", methods = ["POST"])
def crearUsuario():
    try:
        #Datos ingresados por el usuario
        datos = request.get_json()
        nombre = datos['nombre']
        apellidoPaterno = datos['apellidoPaterno']
        apellidoMaterno = datos['apellidoMaterno']
        email = datos['email']

        #validamos los campos antes de insertarlos en la bd
        if not nombre:
            return jsonify(error = "Nombre es un campo requerido"), 400
        if not apellidoPaterno:
            return jsonify(error = "Apellido Paterno es un campo requerio"), 400
        if not apellidoMaterno:
            return jsonify(error = "Apellido Materno es un campo requerido"), 400
        if not email:
            return jsonify(error = "Email es un campo requerido"), 400
        if not '@' in email:
            return jsonify(error = "Email no valido"), 400

        #Coneccion a la base de datos
        #con = conexion.conexion
        cursor = conexion.conexion.cursor(dictionary=True)

        #Consulta a la base de datos
        newUser = "INSERT INTO usuario (NombreUsuario, ApellidoPusuario, ApellidoMusuario, Email) VALUES (%s, %s, %s, %s) RETURNING"
        values = (nombre, apellidoPaterno, apellidoMaterno, email)

        #Ejecutamos la consulta
        cursor.execute(newUser, values)

        #Obtenemos el usuario creado
        usuarioCreado = cursor.fetchone()

        # Confirmamos los cambios
        conexion.conexion.commit()

    except Exception as e:

        #Manejamos la excepcion
        #retorna un codigo de respuesta HTTP 500 y un mensaje de error en el cuerpo
        return jsonify(error=str(e)), 500

    #finally:

        #Cerrramos la conexion y el cursor
        #con.close()
        #cursor.close()

    #retorna el diccionario en formato json para el usuario
    return jsonify(mensaje="Usuario creado exitosamente", usuario=usuarioCreado), 201

@app.route('/')
def home():
    return send_file('static/index.html')

    
if __name__ == '__main__':
    app.run(debug=True)
