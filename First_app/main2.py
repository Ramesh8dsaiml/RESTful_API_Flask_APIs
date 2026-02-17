## import flask
from flask import Flask , jsonify

## create flask instance
app = Flask(__name__)


## define function and route 

## '/' , '/about' , '/data'

@app.route('/')
def home():
    return "Welcome to my Website."

@app.route('/about')
def about():
    return """<h1>About Us</h1><br>
              <h2>PW Skills' vision is to permeate through every student/professional's</h2>
              <h3>Thank You for PW skill application.</h3>"""

@app.route('/data')
def data():
    user_data = {"name":"Noorain",
                 "Age" : 23}

    return jsonify(user_data)






## trigger the flask app
if __name__ == '__main__':
    app.run(debug = True)