'''
Name: Jianzhuo Ye
Start Date: 3/5/24
End Date: 3/6/24
Description: This program introduces the use of redirect url
'''

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page <h1>HELLO</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Jianzhuo Ye")) #Type your name

@app.route("/admin123")
def admin123():
    return redirect(url_for("user",name="Sue deer")) #Type your name

if __name__ == "__main__":
    app.run()
