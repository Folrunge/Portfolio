from flask import Flask, render_template, flash, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
	headline1 = "Good morning,  !"
	headline2 = "Good afternoon,  !"
	headline3 = "Good evening,  !"
	return render_template("index.html", headline1=headline1)