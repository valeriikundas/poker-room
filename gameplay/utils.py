import logging
import os
import random
import time
import json

import requests

DJANGO_URL = os.environ.get("DJANGO_URL")


def inform_users(data):
    table_id = data["table_id"]

    while True:
        try:
            response = requests.get(
                f"http://{DJANGO_URL}/api/inform/{table_id}/", json=data, timeout=10
            )
            break
        except (requests.Timeout, requests.ConnectionError):
            logging.fatal("`inform players` error. retrying...")
            time.sleep(5)


def request_action_from_user(table_id, username, action_space):
    try:
        print("actionspacea", action_space)
        response = requests.post(
            f"http://{DJANGO_URL}/api/request_action/{table_id}/{username}/",
            data={"action_space": json.dumps(action_space)},
            timeout=10,
        )
        logging.info(
            f"""request_action table_id={table_id} username={username} data=
                "table_id": {table_id}
                "username": {username}
                "action_space" {action_space}"""
        )
        try:
            action = response.json()
        except Exception as e:
            action = {"status": "error"}
            logging.error(e)
    except (requests.Timeout, requests.ConnectionError):
        action = {"status": "timeout"}

    return action


def find_next_active_player_position_after(active_players, position):
    for i in active_players:
        if i > position:
            return i

    return active_players[0]
