import json
import requests


def read_json(file_path: str):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return dict(data)


url_m = "http://127.0.0.1:5551/dg"


def dg_function():
    try:
        data = read_json(
            "settings.json"
        )  # You need to define a function to read JSON from a file
        print(data)
        print("======================")
        response = requests.post(url=url_m, json=data)
        if response.status_code == 200:
            print("Request sent successfully")
        else:
            print("Error: Status Code", response.status_code)

    except Exception as e:
        print("An exception occurred:", str(e))


# def api_call():
#     url = "http://127.0.0.1:5551/dg1"
#     response = requests.post(
#         url,
#     )
#     data = response.json()
#     return data
