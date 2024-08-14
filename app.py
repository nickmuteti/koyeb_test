from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'We are testing to see if it is working!'


if __name__ == "__main__":
    app.run(port=8000)

