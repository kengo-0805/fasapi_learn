import requests
import json

def main():
    url = 'http://127.0.0.1:8000/item/' # エンドポイントURL
    body = {
        "name": "T-shirt",
        "description": "stsssss",
        "price": 5980,
        "tax": 1.1
    }
    res = requests.post(url, json=body) # POSTリクエストを送信
    print(res.json())

if __name__ == "__main__":
    main()