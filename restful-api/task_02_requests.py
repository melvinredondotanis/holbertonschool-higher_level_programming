#!/usr/bin/env python
"""Task 2: Requests"""

import csv
import requests


def fetch_and_print_posts():
    """Fetches posts from a RESTful API and prints them."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetches posts from a RESTful API and saves them to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'],
                                 'title': post['title'],
                                 'body': post['body']
                                 })
