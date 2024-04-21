from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the homepage'

@app.route('/hello')
def hello():
    return 'Hello, World!'

# New route for testing invalid route
@app.route('/invalid-route')
def invalid_route():
    return jsonify({'error': 'Route not found'}), 404

# New route for testing POST method not allowed
@app.route('/post-method', methods=['GET'])
def post_method_not_allowed():
    if request.method == 'POST':
        return jsonify({'error': 'Method not allowed'}), 405
    else:
        return jsonify({'message': 'GET method allowed'})

if __name__ == '__main__':
    app.run(debug=True)
