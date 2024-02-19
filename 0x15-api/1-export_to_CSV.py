#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    username = user.get("username")
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params)
    todos = todos.json()
    with open("{}.csv".format(user_id), "w", newline="") as data:
        writer = csv.writer(data, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, todo.get("completed"), todo.get("title")]
         ) for todo in todos]
