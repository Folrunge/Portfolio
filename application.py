from flask import Flask, render_template, flash, redirect, request, url_for
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
	time = datetime.now().time()
	if time.hour > (0) and time.hour < (12):
		headline1 = "Good morning,  !"
		return render_template("index.html", headline1=headline1)
	elif time.hour >= (12) and time.hour < (18):
		headline2 = "Good afternoon,  !"
		return render_template("index.html", headline2=headline2)
	else:
		headline3 = "Good evening,  !"
		return render_template("index.html", headline3=headline3)
	