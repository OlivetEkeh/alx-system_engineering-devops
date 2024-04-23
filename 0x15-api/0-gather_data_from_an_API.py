#!/usr/bin/python3
""" Make an api request """
import requests
from sys import argv

# The API endpoint
base_url = "https://jsonplaceholder.typicode.com"


def fetch_employee_data(_id):
    user = requests.get(f"{base_url}/users/{_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={_id}").json()

    done = []
    total = 0
    for todo in todos:
        total += 1
        if todo['completed']:
            done.append(todo['title'])
    print(f"Employee {user['name']} is done with tasks({len(done)}/{total}):")
    for task in done:
        print(f"\t {task}")


if __name__ == "__main__":
    fetch_employee_data(argv[1])
