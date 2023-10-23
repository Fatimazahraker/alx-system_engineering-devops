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
    response = requests.get(f'{url}/todos?userId={id}')
    todo_data = response.json()
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    print(f'Employee {name} is done with tasks ({done_tasks}/{total_tasks}):')
    for task in todo_data:
        if task['completed']:
            print(f'\t{task["title"]}')


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    todo_employee(employee_id)
