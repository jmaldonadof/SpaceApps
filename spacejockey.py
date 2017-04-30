from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/base")
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)