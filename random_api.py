from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/v1/users', methods=['GET'])
def get_random_users():
    users = [
        {
            'id': i,
            'name': f'User {i}',
            'email': f'user{i}@example.com'
        } for i in range(1, 11)
    ]
    
    random_user = random.choice(users)
    return jsonify(random_user)

if __name__ == '__main__':
    app.run()