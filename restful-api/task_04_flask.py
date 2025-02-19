#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def user():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_usr(username):
    if username not in users:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    else:
        return jsonify(users[username])


@app.route('/add_user', methods=['POST'])
def add_usr():
    new_user = request.get_json()
    if 'username' not in new_user:
        return jsonify({"error": "Nom d'utilisateur requis"}), 404
    username = new_user['username']
    users[username] = {"username": new_user.get('username'), "name": new_user.get(
        'name'), "age": new_user.get('age'), "city": new_user.get('city')}
    return jsonify({"message": "Utilisateur ajouté", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
