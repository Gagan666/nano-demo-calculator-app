import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello World!"

@app.route('/calculator/add',methods=['POST'])
def add():
    data = request.get_json()
    first = data.get('first',0)
    second = data.get('second',0)
    res = first+second
    return jsonify({'result':res})

@app.route('/calculator/subtract',methods=['POST'])
def sub():
    data = request.get_json()
    first = data.get('first',0)
    second = data.get('second',0)
    res = first-second
    return jsonify({'result':res})


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')