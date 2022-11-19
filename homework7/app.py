from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    print(data)
    return data

def test():
    requests.post('http://127.0.0.1:5000/add_user', json={'name': 'test'})

if __name__ == '__main__':
    app.run()


