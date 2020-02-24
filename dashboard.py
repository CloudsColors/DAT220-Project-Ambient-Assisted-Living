from flask import Flask, render_template

app = Flask(__name__, template_folder="./view/")

@app.route('/')
def hello_world():
    return render_template("index.html", name="Andreas")

if __name__ == "__main__":
    app.run(debug=True)