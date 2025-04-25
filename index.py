
from flask import Flask,render_template,request
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/interest")
def interest():
    return render_template("interest.html")

@app.route("/Resume")
def Resume():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("Resume.html", datetime = str(now))

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    c = request.values.get("c")

    return render_template("welcome.html", name=user,pu=c)


    



if __name__ == "__main__":
    app.run()
    #serve(app,host='0.0.0.0',port=8080)
