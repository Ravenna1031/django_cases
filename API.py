import requests

server = "http://127.0.0.1:8000"


def nums(a, b):
    address = "/nums"
    url = server + address
    data = {
        "a": a,
        "b": b
    }
    response = requests.get(url=url, params=data)
    return response