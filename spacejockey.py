from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/facts")
def facts():
    return render_template("facts.html")


if __name__ == "__main__":
    app.run(debug=True)