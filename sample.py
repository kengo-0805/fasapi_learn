import requests
import json

def main():
    url = "http://127.0.0.1:8000"
    data = {
        "x": 3.5,
        "y": 2.0
    }
    res = requests.post(url, json=data)  # POSTリクエストを送信
    print(res.json())

if __name__ == "__main__":
    main()