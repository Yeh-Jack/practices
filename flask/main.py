from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world !!"


@app.route("/flask/")
def hello_flask():
    return "Hello from flask !!"


if __name__ == "__main__":
    # app.run() # Use Flask default port : 5000
    app.run(debug=True, host="0.0.0.0", port="8080")
