#import firebase_admin
#from firebase_admin import credentials, firestore
#cred = credentials.Certificate("serviceAccountKey.json")
#firebase_admin.initialize_app(cred)


from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "資管二A 蔡承宙<br>"
    X +="<a href=/about>個人網頁</a><br>"


    return X

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
   app.run()
#改動測試3