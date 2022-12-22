import pandas
from flask import Flask,render_template,jsonify,request,json,send_file




app = Flask(__name__)

@app.route("/")
def home():
    if request.is_json :
        text = request.args.get("datau")
        df = pandas.read_csv("handwashing_report.csv")
        l = len(df)
        print(len(df))
        df = json.loads(df.to_json())
        return jsonify({"report":df,
        "l":l})


    return render_template("home.html")
@app.route("/report")
def report():
    if request.is_json :
        text = request.args.get("datau")
        df = pandas.read_csv("handwashing_report.csv")
        l = len(df)
        print(len(df))
        df = json.loads(df.to_json())
        return jsonify({"report":df,
        "l":l})
    return render_template("report.html")

@app.route("/download")
def download_file():
    path = "handwashing_report.csv"
    return send_file(path,as_attachment=True)

@app.route("/instagram")
def insta():
    path = 'templates/img/instagram.png'
    return send_file(path)
if __name__ == "__main__":
    app.run(debug=True)
