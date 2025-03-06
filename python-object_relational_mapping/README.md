# Python - Object-relational mapping

## General

How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table

## Requirements 

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
Your files will be executed with MySQLdb version 2.0.x
Your files will be executed with SQLAlchemy version 1.4.x
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
You are not allowed to use execute with sqlalchemy

## Tasks

0. Get all states
1. Filter states
2. Filter states by user input
3. SQL Injection...
4. Cities by states
5. All cities by state
6. First state model
7. All states via SQLAlchemy
8. First state
9. Contains `a`
10. Get a state
11. Add a new state
12. Update a state
13. Delete states
14. Cities in state

## Documentation

1. Connexion à une base de données MySQL depuis un script python

Pour intéragir avec MySQL en python, on utilise la bibliothèque `mysql-connector-python` ou `MySQLdb`

Connexion à la base de données :

Voici un exemple de connexion à une base de données MySQL :

```python
import mysql.connector

# Connexion à MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="nom_de_la_base"
)
cursor = conn.cursor()
```

2. Sélectionner des lignes dans une table MySQL depuis un script Python

Exécuter une requête SELECT :

```python
cursor.execute("SELECT * FROM nom_de_la_table")
resultats = cursor.fetchall()

for ligne in resultats:
    print(ligne)
```
Fermer la connexion : 

```python
cursor.close()
conn.close()
```

3. Insérer des lignes dans une table  MySQL depuis un script python

Exécuter une requête INSERT

```python
requete = "INSERT INTO nom_de_la_table (colonne1, colonne2) VALUES (%s, %s)"
valeurs = ("valeur1", "valeur2")
cursor.execute(requete, valeurs)
conn.commit()
```

Récupérer l'ID de la ligne insérée

```python
print("ID inséré:", cursor.lastrowid)
```

4. Qu'est ce qu'un ORM

ORM (Object-Relational Mapping) est une technique permettant d'interagir avec une base de données via des objets Python au lieu d'utiliser directement le SQL.
L'ORM permet de simplifier la gestion des bases de données en évitant d'écrire du SQL brut.
L'ORM le plus utilisé en Python  est SQLAlchemy.

5. Mapper une classe python à une table MySQL avec SQLAlchemy

Création d'une classe correspondant à une table

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50))
    email = Column(String(100))

# Connexion à MySQL
engine = create_engine("mysql+mysqlconnector://user:password@localhost/nom_de_la_base")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Ajouter un utilisateur
nouvel_utilisateur = Utilisateur(nom="Jean Dupont", email="jean.dupont@example.com")
session.add(nouvel_utilisateur)
session.commit()
```

Récupérer des données avec SQLAlchemy

```python
utilisateurs = session.query(Utilisateur).all()
for user in utilisateurs:
    print(user.nom, user.email)
```

Fermer la session 

```python
session.close()
```