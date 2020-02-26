from flask import Flask, render_template

import HealthMonitoring.OverviewSystem as oss

app = Flask(__name__, template_folder="./view/")

@app.route('/')
def hello_world():
    return render_template("index.html", name="Andreas")

@app.route('/medical')
def medical():
    hb, sc = oss.heartBeatandStep()
    return render_template("medical.html", hb=hb, sc=sc )

if __name__ == "__main__":
    app.run(debug=True)