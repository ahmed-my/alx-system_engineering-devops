#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.

This script takes an employee ID as a command-line argument and exports
the corresponding user information and to-do list to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    # Get the employee ID from the command-line argument
    user_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using the provided employee ID
    # user = requests.get(url + "users/{}".format(user_id)).json()
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    username = user.get("username")

    # Fetch the to-do list for the employee using the provided employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params)
    todos = todos.json()

    # Create a dictionary containing the user and to-do list information
    data_to_export = {
        user_id: [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            for todo in todos
        ]
    }

    # Write the data to a JSON file with the employee ID as the filename
    with open("{}.json".format(user_id), "w") as data:
        json.dump(data_to_export, data, indent=4)
