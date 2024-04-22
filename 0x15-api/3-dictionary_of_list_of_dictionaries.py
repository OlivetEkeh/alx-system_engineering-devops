#!/usr/bin/python3
""" Make a json file conataining api request """
import json
import requests

# The API endpoint
base_url = "https://jsonplaceholder.typicode.com"


def fetch_employee_data():
    users = requests.get(f"{base_url}/users").json()
    todos = requests.get(f"{base_url}/todos").json()
    json_filename = "todo_all_employees.json"

    formatted_todos = {}

    for user in users:
        username, u_id = user.get("username"), user.get("id")
        formatted_todos[u_id] = [{
            "username": username,
            "task": todo["title"],
            "completed": todo["completed"]
            } for todo in [todo for todo in todos if todo["userId"] == u_id]]

    with open(json_filename, 'w') as json_file:
        json.dump(formatted_todos, json_file)


if __name__ == "__main__":
    fetch_employee_data()
