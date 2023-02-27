import requests
from pprint import pprint

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN_KEY = str(os.getenv('TOKEN_KEY'))


def client():
    token = TOKEN_KEY

    headers = {
        "Authorization": token,
    }

    response = requests.get(
        url = "http://127.0.0.1:8000/api/users-profile/",
        headers = headers,
        )
    print("status code: ", response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == "__main__":
    client()