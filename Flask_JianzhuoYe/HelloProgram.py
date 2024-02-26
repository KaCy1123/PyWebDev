'''
Name: Jianzhuo Ye
Start Date: 2/26/24
End Date: 2/26/24
Description: This program is an introduction to using flask and python
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello. This is the main program! <h1>Hello</h1>"

if __name__ == "__main__":
    app.run()
