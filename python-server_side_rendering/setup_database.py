#!/usr/bin/python3

import sqlite3


def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Supprimer les données existantes pour éviter les doublons lors des exécutions répétées
    cursor.execute('DELETE FROM Products')

    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()
    print("Base de données créée et remplie avec succès.")


if __name__ == '__main__':
    create_database()
