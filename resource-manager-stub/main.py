import json

from flask import Flask

edge_list = [
    "edge-router00",
    "edge-router02",
    "edge-router03"
]

robot_list = [
    "gopigo3",
    "turtlebot3",
    "gopigo3_camera"
]

res_json = [
    {
        "name": "edge-router01",
        "addr": "10.244.5.1",
        "namespace": {
            "name": None,
            "ros-master": None
        },
        "boot-cmd": None
    },
    {
        "name": "my-gopigo3",
        "addr": "10.244.5.50",
        "namespace": {
            "name": "sample",
            "ros-master": "ros-master.sample.svc.cluster.local"
        },
        "boot-cmd": None
    }
]

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello !!"

@app.route("/resources/edge/", methods=["GET"])
def get_edge_routers():
    # エッジルータの一覧を返す
    return json.dumps(edge_list)

@app.route("/resources/edge/<string:name>/", methods=["PUT"])
def create_new_edge_router(name):
    # 成功か不成功を返す
    if name in edge_list:
        status = 500
    else:
        status = 200
    
    return "", status

@app.route("/resources/edge/<string:name>/update/", methods=["POST"])
def update_robots_with_edge_router(name):
    # ネームスペースやROSの情報を返す
    return json.dumps(res_json)

@app.route("/resources/robot/", methods=["GET"])
def get_robots():
    # ロボットの一覧を返す
    return json.dumps(robot_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
