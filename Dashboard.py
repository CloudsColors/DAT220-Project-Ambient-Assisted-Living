from flask import Flask, render_template, request, redirect



import HealthMonitoring.OverviewSystem as oss
import HealthMonitoring.PatientInput   as pi
app = Flask(__name__, template_folder="./view/")

@app.route('/')
def hello_world():
    return render_template("index.html", name="Andreas")

@app.route('/medical', methods=["GET", "POST"])
def medical():
    if(request.method == "GET"):
        return render_template("medical.html")
    
    if(request.method == "POST"):
        hb, sc = oss.heartBeatandStep()
        return {"heartbeat": hb, "stepcounter": sc}

@app.route('/medical/submit', methods=["POST"])
def submitForm():
    if(request.method == "POST"):
        if(not request.form["glucoseInput"] == None or not request.form["glucoseInput"] == ""):
            pi.glucose_data(request.form["glucoseInput"])

        if(not request.form["bloodInput"] == None or not request.form["bloodInput"] == ""):
            pi.blood_data(request.form["bloodInput"])    
           

    return redirect("http://127.0.0.1:5000/medical", code=301)

    

        
        




if __name__ == "__main__":
    app.run(debug=True)