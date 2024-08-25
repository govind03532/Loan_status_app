from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_api():
    return "<p>Good morning from Shubham</p>"


if __name__ == "__main__":
    app.run(debug = True)
