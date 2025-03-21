#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    # Lire les données depuis le fichier JSON
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)

# Fonction pour lire le fichier JSON


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Fonction pour lire le fichier CSV


def read_csv_file(file_path):
    products = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Convertir l'ID en entier pour une comparaison cohérente
            row['id'] = int(row['id'])
            # Convertir le prix en float
            row['price'] = float(row['price'])
            products.append(row)
    return products

# Fonction pour lire depuis la base de données SQLite


def read_sql_database(db_path):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        # Configurer pour obtenir les résultats en tant que dictionnaires
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Exécuter la requête pour récupérer tous les produits
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()

        # Convertir chaque ligne en dictionnaire
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })

        conn.close()
        return products
    except sqlite3.Error as e:
        raise Exception(f"Erreur de base de données: {str(e)}")


@app.route('/products')
def products():
    # Récupérer les paramètres de requête
    source = request.args.get('source', default=None)
    product_id = request.args.get('id', default=None)

    # Vérifier si la source est valide
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Lire les données en fonction de la source
    try:
        if source == 'json':
            products_data = read_json_file('products.json')
        elif source == 'csv':
            products_data = read_csv_file('products.csv')
        else:  # source == 'sql'
            products_data = read_sql_database('products.db')
    except Exception as e:
        return render_template('product_display.html', error=f"Error reading data: {str(e)}")

    # Filtrer par ID si fourni
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [
                p for p in products_data if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            products_data = filtered_products
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

    # Rendre le template avec les données
    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
