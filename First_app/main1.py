# import flask 
from flask import Flask

## create a flask instance 
app= Flask(__name__)

## define function and route
@app.route('/')
def home():
     return "hello ramesh"



##trigger the flask app
if __name__ == '__main__':
     app.run()
