from flask import Flask, render_template
import flask

import HealthMonitoring.OverviewSystem as oss

app = Flask(__name__, template_folder="./view/")

@app.route('/')
def hello_world():
    return render_template("index.html", name="Andreas")

@app.route('/medical', methods=["GET", "POST"])
def medical():
    if(flask.request.method == "GET"):
        hb, sc = oss.heartBeatandStep()
        return render_template("medical.html", hb=hb, sc=sc )
    if(flask.request.method == "POST"):
        hb, sc = oss.heartBeatandStep()
        return {"heartbeat": hb, "stepcounter": sc}

if __name__ == "__main__":
    app.run(debug=True)