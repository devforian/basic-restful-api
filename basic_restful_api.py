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

def delete_element_dictionary(dic, id):
    del_info = dic.pop(id)
    # del_info -> DB

def fix_element_dictionary(dic, old_id, new_id):
    delete_element_dictionary(dic, old_id)
    append_dictionary(dic, new_id)

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
# Windows cmd> curl -d "{""id"":7}" -H "Content-Type: application/json" -X POST http://localhost:5000/client/list
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
# Windows cmd>curl -d "{""id"":10}" -H "Content-Type: application/json" -X PUT http://localhost:5000/client/list/7
@app.route("/client/list/<int:client_id>", methods=["PUT"])
def put_client(client_id):
    old_client = clients.get(client_id)
    new_client = request.get_json()
    fix_element_dictionary(clients, old_client["id"], new_client["id"])
    return jsonify(new_client), 201
            

if __name__ == "__main__":
    app.run(debug=True)

