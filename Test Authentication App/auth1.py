from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return "Login Here."


@app.route('/profile', methods=['GET'])

def profile():
    return "Welcome to your Profile!"

if __name__ == '__main__':
    app.run(debug=True)