from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CROS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)


@app.route('/api/afiliado/<int:id>')
@cross_origin()
def getUserInfo(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, nombre, apellidos, email, telefono FROM ourcustomers WHERE id = ' + str(id) + '; ')
    data = cur.fetchall()
    content = {}
    for row in data:
        content = {'id': row[0], 'firstname': row[1], 'lastname': row[2], 'email': row[3], 'telefono': row[4]}

    return jsonify(content)


@app.route('/api/afiliado')
def getAllUsers():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, nombre, apellidos, email, telefono FROM ourcustomers')
    data = cur.fetchall()
    resultado = []
    for row in data:
        content = {'id': row[0], 'firstname': row[1], 'lastname': row[2], 'email': row[3], 'telefono': row[4]}
        resultado.append(content)
    return jsonify(resultado)


@app.route('/api/afiliado', methods=['POST'])
def compUser():
    if 'id' in request.json:
        updateUser()
    else:
        createUser()


def createUser():
    request.json['nombre']
    svuser = mysql.connection.cursor()
    svuser.execute("INSERT INTO `ourcustomers` (`id`, `nombre`, `apellidos`, `email`, `telefono`) VALUES (NULL, %s , %s, %s, %s);",
                   (request.json['nombre'], request.json['apellidos'], request.json['email'], request.json['telefono']))
    mysql.connection.commit() # realiza la ejecucion del comando de la insercion
    return 'user saved'


# @app.route('/api/afiliado', methods=['PUT'])
def updateUser(id):
    request.json['nombre']
    svuser = mysql.connection.cursor()
    svuser.execute("UPDATE `ourcustomers` SET `nombre` = %s, `apellidos` = %s, `email` = %s, `telefono` = %s WHERE `ourcustomers`.`id` = %s;",
                   (request.json['nombre'], request.json['apellidos'], request.json['email'], request.json['telefono'], request.json['id']))
    mysql.connection.commit() # realiza la ejecucion del comando de la insercion
    return 'user saved'


@app.route('/api/afiliado/<int:id>', methods=['DELETE'])
def deleteUser(id):
    dluser = mysql.connection.cursor()
    dluser.execute("DELETE FROM `ourcustomers` WHERE `ourcustomers`.`id` = " + str(id) + ";")
    mysql.connection.commit()
    return 'deleted'


@app.route('/')
def Index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(None, 3000, True)