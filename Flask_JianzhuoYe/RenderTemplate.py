'''
Name: Jianzhuo Ye
Start Date: 3/6/24
End Date: 3/8/24
Description: This program introduces the use of templates into Flask.
'''

from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("personinfo.html")

@app.route("/1")
def moreinfo():
    return render_template("anotherinfo.html")

if __name__ == "__main__":
    app.run()
