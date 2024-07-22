# Reference
# https://maru1000.tistory.com/90
# https://dev-cool.tistory.com/32
from flask import Flask, request, jsonify

app = Flask(__name__)

# dictionary
clients = {
   1: {"id": 1, "name": "Client1"},
   2: {"id": 2, "name": "Clinet2"},
   3: {"id": 3, "name": "Clinet3"},
   4: {"id": 4, "name": "Clinet4"},
   5: {"id": 5, "name": "Clinet5"}
}

# Append element into dictionary
def append_dictionary(dic, id):
    dic[id] = {"id": id, "name": "Client"+str(id)}

# GET /api/hello
@app.route("/api/hello")
def hello():
    return "Hello, World!"

# GET /client/list
# REST API 설계 규칙 1. 소문자를 사용하라
# REST API 설계 규칙 2. Hyphen(-)을 사용하라
# REST API 설계 규칙 3. 마지막에 Slash(/)를 포함하지 마라
@app.route("/client/list")
def get_clients():
    return jsonify(list(clients.values()))

# GET /client/list/{id}
@app.route("/client/list/<int:client_id>")
def get_client(client_id):
    client = clients.get(client_id)
    if client:
        return jsonify(client)
    return jsonify({"message": "Client not found"}), 404

# POST /client/list
# {id: n}
# curl -d "{""id"":7}" -H "Content-Type: application/json" -X POST http://localhost:5000/api/clients
# Reference: https://blog.naver.com/wideeyed/221350638501
@app.route("/client/list", methods=["POST"])
def post_client():
    client = request.get_json()
    if client:
        print(client)
        client_id = client["id"]
        append_dictionary(clients, client_id)
    return jsonify(client), 201
    

# PUT /client/list/{id}
@app.route("/client/list/<int:client_id>", methods=["PUT"])
def put_client(client_id):
    client = clients[client_id]
    if client:
        print(client)
    return jsonify(client), 201
            

if __name__ == "__main__":
    app.run(debug=True)

