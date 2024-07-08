import sqlite3
import hashlib
import re
from flask import Flask, request, jsonify

def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, password_hash TEXT)''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(name, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, password_hash) VALUES (?, ?)", (name, hash_password(password)))
    conn.commit()
    conn.close()

def validate_user(name, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE name = ?", (name,))
    result = c.fetchone()
    conn.close()
    if result:
        stored_password_hash = result[0]
        return stored_password_hash == hash_password(password)
    return False

def is_valid_username(username):
    return re.match("^[a-zA-Z0-9_.-]+$", username) is not None

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    if validate_user(name, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Login failed"}), 401

def main_menu():
    create_database()
    while True:
        try:
            cant = int(input("Por favor ingrese la cantidad de usuarios que desea agregar (o 0 para salir del programa): "))
            if cant == 0:
                print("Saliendo del programa.")
                break
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue

        print("Añada los usuarios a la lista, por favor.")
        for i in range(cant):
            while True:
                name = input(f"Ingrese el nombre del integrante {i+1} (solo caracteres alfanuméricos, guiones bajos, puntos o guiones): ")
                if is_valid_username(name):
                    break
                else:
                    print("El nombre de usuario contiene caracteres no permitidos. Inténtelo de nuevo.")

            password = input(f"Ingrese su contraseña para {name}: ")
            add_user(name, password)
            print(f"El usuario {name} añadido con éxito.")
        
        while True:
            continuar = input("¿Desea agregar más usuarios a la lista? (s/n): ").lower()
            if continuar in ['s', 'n']:
                break
            print("Por favor, ingrese 's' para continuar o 'n' para salir del programa.")

        if continuar == 'n':
            print("Saliendo del programa.")
            print("Gracias por su preferencia")
            break

if __name__ == '__main__':
    main_menu()
    app.run(port=5800)
