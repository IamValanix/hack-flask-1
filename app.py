from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({'payload':'success'})

@app.route("/user", methods=["POST"])
def create_user():
    return jsonify({'payload': 'success'})

@app.route("/user", methods=['DELETE'])
def del_user():
    return jsonify({'payload':'success'})

@app.route("/user", methods=['PUT'])
def put_user():
    return jsonify({'payload':'success'})

@app.route("/api/v1/users", methods=["GET"])
def get_users2():
    return jsonify({'payload':[]})

@app.route("/api/v1/user", methods=["POST"])
def get_users3():
    email = request.args.get('email')
    name = request.args.get('name')

    return jsonify({
        'payload': {
            'email': email,
            'name': name,
        }
    })

if __name__ == "__main__":
    app.run(debug=True)