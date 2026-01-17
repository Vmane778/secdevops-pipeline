from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Secure Python!'

if __name__ == '__main__':
    app.run(debug=True, port=8080)