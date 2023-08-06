import requests
from flask import Flask, request, jsonify

app = Flask(_name_)


@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello World!", 200

@app.route('/calculator/add',methods=['POST'])
def add():
    data = request.get_json()
    first = data.get('first',0)
    second = data.get('second',0)
    res = first+second
    return jsonify({'result':res}),200

@app.route('/calculator/subtract',methods=['POST'])
def sub():
    data = request.get_json()
    first = data.get('first',0)
    second = data.get('second',0)
    res = first-second
    return jsonify({'result':res}),200


if _name_ == '_main_':
    app.run(port=8080,host='0.0.0.0')