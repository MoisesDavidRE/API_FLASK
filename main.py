from flask import Flask, jsonify, request
import mysql.connector as cnx

app = Flask(__name__)

config = {
    "host": "localhost",
    "port": 3306,
    "user": "david",
    "password": "1234",
    "database": "api_matchpet"
}
cnxx = cnx.connect(**config)
x=0
@app.route("/")
def index():
    return "ola sin h"

@app.route("/user/<idUser>")
def get_user(idUser):
    
    cur = cnxx.cursor()
    cur.execute("SELECT * FROM user WHERE idUser = %s", (idUser,))
    user = cur.fetchone()
    cur.close()
    if user:
        columns = [
            "idUser", "email", "pass", "name", "lastName1", "lastName2", 
            "profileImage", "userAge", "state", "city", "socialNetwork", 
            "description", "created_at", "updated_at", "deleted_at"
        ]
        user_data = dict(zip(columns, user))
        return jsonify(user_data)
    return jsonify({"error": "User not found"}), 404

@app.route("/pets/<idPet>")
def get_user_name(idUser    ):
    cur = cnxx.cursor()
    cur.execute("SELECT idUser,name FROM user WHERE idUser = %s", (idUser,))
    user = cur.fetchone()
    cur.close()
    if user:
        columns = ["idUser", "name"]
        user_data = dict(zip(columns, user))
        return jsonify(user_data)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=4000)
    