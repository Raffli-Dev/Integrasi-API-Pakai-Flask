from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-user/<id>', methods=['GET'])
def get_user(id):
    user_data = [
        {
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
        },
        {
            "sugestion": [
                {
                    "Alamat": "Magetan",
                    "Nomer_Hp": "085730183893",
                    "Propinsi": "Jawa Timur"
                },
                {
                    "Alamat": "Madiun",
                    "Nomer_Hp": "085730183893",
                    "Propinsi": "Jawa Timur"
                },
                {
                    "Alamat": "Magetan",
                    "Nomer_Hp": "085730183893",
                    "Propinsi": "Jawa Timur"
                }
            ]
        }
    ]

    test = request.args.get("test")
    if test:
        user_data[0]["test"] = test

    return jsonify(user_data), 200

#Best Practice API
@app.route('/practice/<id>', methods=['GET'])
def practice(id):
    user_data = [
        {
            "code": "200",
            "status": "Status OK!!!",
            "data": {
                "Name": "Hello World",
                "age": 21,
                "Address": "Magetan City"
            },
            "errors": {
                "id": [
                    "Product Error"
                ]
            }
        }
    ]

    test = request.args.get("test")
    if test:
        user_data[0]["test"] = test

    return jsonify(user_data), 200




@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
