# module and packages should starts with lower case and and a class starts with lower case
from flask import Flask

# this is creating a flask app and __name__ tell the app that is starting here
app = Flask(__name__)


@app.route(
    "/"
)  # the foward slash is always refers to the home page (it's the main endpoint)
def home():
    return "Hello, world!"


app.run(port=5000)