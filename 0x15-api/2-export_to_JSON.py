#!/usr/bin/python3
""" module doc """
import requests
import sys
import json


def todo_employee(id):
    """ def doc"""
    url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(f'{url}/users/{id}')
    user_data = response.json()
    name = user_data['name']
    username = user_data['username']
    response = requests.get(f'{url}/todos?userId={id}')
    todo_data = response.json()

    with open(f"{id}.json", "w") as f:
        data = {
            id: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username,
                }
                for task in todo_data
            ]
        }
        json.dump(data, f)


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    todo_employee(employee_id)
