#!/usr/bin/python3
""" Make an api request """
import json
import requests
from sys import argv

# The API endpoint
base_url = "https://jsonplaceholder.typicode.com"


def fetch_employee_data(_id):
    user = requests.get(f"{base_url}/users/{_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={_id}").json()
    json_filename = f"{_id}.json"

    todos_details = []
    for todo in todos:
        deets = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": user['username']
                }
        todos_details.append(deets)

    data = {user['id']: todos_details}
    json_string = json.dumps(data)
    with open(json_filename, 'w') as json_file:
        json_file.write(json_string)


if __name__ == "__main__":
    fetch_employee_data(argv[1])
