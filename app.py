#integration API Data
from flask import Flask,request,jsonify

app=Flask(__name__)
@app.route('/get-user/<id>')
def home(id):
    user_data = [{
        "data": [
            {
                "user_id": id,
                "nama": "raffli",
                "umur": "21"
            },
            {
                "user_id": id,
                "nama": "GG",
                "umur": "21"
            }
        ]
    }]

    test = request.args.get("test")
    if test:
        user_data[0]["test"] = test

    return jsonify(user_data), 200

@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)