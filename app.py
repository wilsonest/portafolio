from turtle import title
from flask import Flask, redirect, render_template, request, make_response

app = Flask(__name__)

items = ["Java","python-Flask","Javascript","C#","NodeJs"]
mas = ["Sql Server", "MySql"]

@app.route("/")
def index():
    control_info = request.remote_addr
    render = make_response(redirect("/inicio"))
    render.set_cookie("control_info", control_info)
    return render

@app.route("/inicio")
def info():
    user_ip = request.cookies.get("control_info")
    context = {
        "user_ip": user_ip,
        "items" : items,
        "mas" : mas
    }

    return render_template("base.html", **context)

@app.route("/java")
def java():
    data = {
        'titulo' : 'Java'
    }

    return render_template('java.html', **data)

@app.route("/python")
def python():
    data = {
        'titulo' : 'Python'
    }

    return render_template('python.html', **data)

@app.route("/C")
def C():
    data = {
        'titulo' : 'C#'
    }

    return render_template('C#.html', **data)

@app.route("/NodeJs")
def frame():
    data = {
        'titulo' : 'NodeJs'
    }

    return render_template('NodeJs.html', **data)

@app.route("/bd")
def bd():
    data = {
        'titulo' : 'Data base'
    }

    return render_template('bd.html', **data)

@app.route("/wilson")
def wilson():
    data = {
        'titulo' : 'wilson'
    }

    return render_template('wilson.html', **data)
app.run(debug=True)

