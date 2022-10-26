import pyjokes
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello! I am Flask.'
    category='neutral' # values are : all, chuck, neutral
    joke = pyjokes.get_joke(category=category)
    return joke

if __name__ == '__main__':
    # Note the extra host argument. If we didn't have it, our Flask app
    # would only respond to requests from inside our container
    app.run(host='0.0.0.0')
