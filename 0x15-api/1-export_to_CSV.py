#!/usr/bin/python3
""" Make a csv from the api request """
import csv
import requests
from sys import argv

# The API endpoint
base_url = "https://jsonplaceholder.typicode.com"


def fetch_employee_data(_id):
    user = requests.get(f"{base_url}/users/{_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={_id}").json()
    csv_filename = f"{_id}.csv"

    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user['id'], user['username'], todo['completed'],
                            todo['title']])


if __name__ == "__main__":
    fetch_employee_data(argv[1])
