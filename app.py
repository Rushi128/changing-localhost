from http import server
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index page\n"

@app.route('/apis', subdomain = 'api')
def function1():
    return "This is test api\n"


if __name__ == "__main__":
    app.config['SERVER_NAME'] = 'rushi.com:5000'
    app.run(debug=True)
