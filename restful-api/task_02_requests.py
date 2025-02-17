#!/usr/bin/python

import requests  # type: ignore
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Erreur lors de la récupération des posts")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        formatted_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(formatted_posts)

        print("Données enregistrées dans posts.csv")
    else:
        print("Erreur lors de la récupération des posts")
