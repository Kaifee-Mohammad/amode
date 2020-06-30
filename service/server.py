from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(message='Hello from Server')


@app.route('/user')
def user():
    name = request.args.get('name')
    return '<h1>Hello ' + name + '</h1>'


@app.route('/not_found')
def no_resource():
    return jsonify(message='not found'), 404


@app.route('/param/<int:age>/<string:name>')
def param(age: int, name: str):

    if age > 18:
        return jsonify(message=name + ', you are eligible to vote.'), 200

    return jsonify(message='you need to wait')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
