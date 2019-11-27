import time
import json

import requests

name = "edge-router01"
devices_json = [
    {
        "name": name,
        "addr": "10.244.5.1",
        "type": "edge",
        "model": None,
        "spec": {},
        "status": 2,
        "stat": {
            "ifaces": [
                {
                   "name": "lo",
                    "speed": 10,
                    "inOctets": 19815,
                    "outOctets": 19815,
                    "inDicards": 0,
                    "outDiscards": 0,
                },
                {
                    "name": "enxb827eb48fd4e",
                    "speed": 10,
                    "inOctets": 0,
                    "outOctets": 0,
                    "inDicards": 0,
                    "outDiscards": 0,
                },
                {
                    "name": "wlan0",
                    "speed": 0,
                    "inOctets": 222414717,
                    "outOctets": 595993,
                    "inDicards": 1299858,
                    "outDiscards": 0,
                }
            ],
            "cpu": {
                "rate": 80
            },
            "disk": {
                "size": 29649688,
                "used": 7772376,
                "rate": 27
            },
        }
    },
    {
        "name": "my-gopigo3",
        "addr": "10.244.5.50",
        "type": "robot",
        "model": "gopigo3",
        "spec": {
            "camera": "arducam miniモジュール (2メガピクセル)",
            "raspi": "raspberry pi 3 model b+"
        },
        "status": 5,
        "stat": {
            "ifaces": [
                {
                   "name": "lo",
                    "speed": 10,
                    "inOctets": 19815,
                    "outOctets": 19815,
                    "inDicards": 0,
                    "outDiscards": 0,
                },
                {
                    "name": "enxb827eb48fd4e",
                    "speed": 10,
                    "inOctets": 0,
                    "outOctets": 0,
                    "inDicards": 0,
                    "outDiscards": 0,
                },
                {
                    "name": "wlan0",
                    "speed": 0,
                    "inOctets": 222414717,
                    "outOctets": 595993,
                    "inDicards": 1299858,
                    "outDiscards": 0,
                }
            ],
            "cpu": {
                "rate": 80
            },
            "disk": {
                "size": 29649688,
                "used": 7772376,
                "rate": 27
            },
        }
    }
]
devices_json = json.dumps(devices_json)

if __name__ == "__main__":
    url = "http://192.168.189.230:8081"

    print("Starting Device Manager Stub !!")
    try:
        # エッジルータに同一の名前が登録されているか確認
        edge_list = requests.get(
            f"{url}/resources/edge",
            timeout=4)

        # エッジルータを登録
        response = requests.put(
            f"{url}/resources/edge/{name}",
            timeout=4)
    except Exception as e:
        print(e, "\nfinished")

    while True:
        # Resource Managerにデータを送信
        try:
            response = requests.post(
                f"{url}/resources/edge/{name}/update",
                devices_json,
                headers={'content-type': 'application/json'},
                timeout=4)
        except Exception as e:
            print(e)

        time.sleep(1)

