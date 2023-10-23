#!/usr/bin/python3
""" module doc """
import requests
import sys


def todo_employee(id):
    """ def doc"""
    url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(f'{url}/users/{id}')
    user_data = response.json()
    name = user_data['name']
    username = user_data['username']
    response = requests.get(f'{url}/todos?userId={id}')
    todo_data = response.json()

    with open(f'{id}.csv', 'w') as f:
        for todo in todo_data:
            data = f'"{id}","{username}","{todo.get("completed")}",'
            data2 = f'"{todo.get("title")}"\n'
            f.write(data+data2)


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    todo_employee(employee_id)
