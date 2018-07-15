from flask import Flask, render_template, flash, redirect, request, url_for
from datetime import datetime

app = Flask(__name__, template_folder='templates')
#Array for holding navbar names
names = ["Home", "About me", "Projects", "Hobby"]

@app.route("/")
def index():
	#Function for getting local server time
	time = datetime.now().time()
	if time.hour > 0 and time.hour < 12:
		headline = "Good morning,  !"
	elif time.hour >= 12 and time.hour < 18:
		headline = "Good afternoon,  !"
	else:
		headline = "Good evening,  !"
	#Return for template with headers and ul> li	
	return render_template("index.html", headline=headline, names=names)
