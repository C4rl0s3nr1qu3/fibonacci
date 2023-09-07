from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fibonacci/<int:n>', methods=['GET'])
def fibonacci(n):
    if n < 0:
        return jsonify(error='Invalid index'), 400

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return jsonify(fibonacci_value=a)

if __name__ == '__main__':
    app.run()