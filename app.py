from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")
    if not name:
        name = "Ririn"
    return f"<h2>Halo, {name}! Selamat datang di flask first App </h2>"

if __name__ == "__main__":
    app.run(debug=True)            