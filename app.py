#integration API Data
from flask import Flask,request,jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://latihan:caplin11@ac-s43qydu-shard-00-00.xrmw0we.mongodb.net:27017,ac-s43qydu-shard-00-01.xrmw0we.mongodb.net:27017,ac-s43qydu-shard-00-02.xrmw0we.mongodb.net:27017/?ssl=true&replicaSet=atlas-b6z32o-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Latihan
db = client.api_integration

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
        }]
    
    db.api.insert_one(user_data)
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