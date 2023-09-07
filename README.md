# fibonacci
 Fibonacci
 
 To implement a REST API that returns the Fibonacci value for a given index, the following steps must be followed:

1. Choose a programming language and configure a REST API framework or library, in this case Python and Flask were used.

2. Define the route or endpoint that will receive the index "n" as a parameter in the API request.

3. Implement the Fibonacci logic to calculate the value corresponding to the given index, for this the following procedure was used.
    - Initialize two variables, "a" and "b", with initial values 0 and 1.
    - Iterate n times, updating the values of "a" and "b" by exchanging and adding them.
    - After the loop, "a" will contain the Fibonacci value for the given index.

4. Return the calculated Fibonacci value as a response from the API.

The source code of the implementation was developed in Python using Flask, it is the following


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
	

With this implementation, you can send a GET request to 
http://127.0.0.1:5000/fibonacci/3 and receive the response {"fibonacci_value": 2}. 
Similarly, http://127.0.0.1:5000/fibonacci/6 will return {"fibonacci_value": 8}.	


