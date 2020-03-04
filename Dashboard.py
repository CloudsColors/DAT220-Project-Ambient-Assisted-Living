from flask import Flask, render_template, request, redirect, jsonify

import datetime

import HealthMonitoring.OverviewSystem as oss
import HealthMonitoring.PatientInput   as pi
import HomeAccess.DoorManager as dm
import HomeAccess.WindowManager as wm
import AlarmController.SmokeAlarm as acsa
import CompositeLogic.CompositeLogicController as comp
import csv, os

app = Flask(__name__, template_folder="./view/")


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login/submit', methods=["POST"])
def login_submit():
    if(request.method == "POST"):
        if(request.form['uname'] == "Andreas"):
            return redirect("http://127.0.0.1:5000/index", code=301)
        else:
            return redirect("http://127.0.0.1:5000/", code=301)


@app.route('/index')
def hello_world():
    return render_template("index.html", name="Andreas")

@app.route('/medical', methods=["GET", "POST"])
def medical():
    hb = oss.heartbeat_data()
    sc = oss.stepcounter_data()
    if(request.method == "GET"):
        bp = oss.bloodpressure_data() # These are lists
        gc = oss.glucose_data() # These are lists
        cp = comp.get_alarm_detection() # These are lists
        return render_template("medical.html", bp = bp, gc = gc, hb = hb, sc = sc, cp=cp)
    if(request.method == "POST"):
        return {"heartbeat": hb, "stepcounter": sc}

@app.route('/medical/submit', methods=["POST"])
def submitForm():
    if(request.method == "POST"):
        if(not(request.form["glucoseInput"] == None or request.form["glucoseInput"] == "")):
            pi.glucose_data(request.form["glucoseInput"])
        if(not(request.form["bloodInput"] == None or request.form["bloodInput"] == "")):
            pi.blood_data(request.form["bloodInput"])    
    return redirect("http://127.0.0.1:5000/medical", code=301)


@app.route('/social', methods=["GET"])
def social():
    cp=comp.get_alarm_detection()
    return render_template("social.html", cp = cp)

@app.route('/security', methods=["GET", "POST"])
def security():
    if(request.method == "GET"):
        return render_template("security.html", dm=dm.get_door_status(), wm=wm.get_window_status(), acsa=acsa.get_smoke_status(), cp=comp.get_alarm_detection())
    if(request.method == "POST"):
        entityDict = {}
        doorData = dm.get_door_status()
        windowData = wm.get_window_status()
        smokeData = acsa.get_smoke_status()
        for x in doorData:
            entityDict[x[0]] = x[1]
        for y in windowData:
            entityDict[y[0]] = y[1]
        for z in smokeData:
            entityDict[z[0]] = z[1]
        return entityDict

@app.route('/composite', methods=["GET", "POST"])
def composite():
    if (request.method == "POST"):
        print(request.json)
        r = csv.reader(open(os.path.dirname(__file__)+"/DataStorage/data/compositedata.csv"))
        lines = list(r)
        lines[1][0] = 'smoke detected'
        lines[1][1] = 'alert all'
        writer = csv.writer(open(os.path.dirname(__file__)+"/DataStorage/data/compositedata.csv", 'w', newline=""))
        writer.writerows(lines)
        return "hello"
    if (request.method == "GET"):
        return render_template("composite.html", cp=comp.get_alarm_detection())

if __name__ == "__main__":
    app.run(debug=True)