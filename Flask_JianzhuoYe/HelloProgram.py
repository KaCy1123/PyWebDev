'''
Name: Jianzhuo Ye
Start Date: 2/27/24
End Date: 2/27/24
Description: This program is an introduction to using flask and python and produces multiple lines on the web page
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    output = "Hello. This is the main program! <h1>Hello</h1>";
    output = output + "<p>This is a paragraph</p>This is not a paragraph";
    output = output + "<br>This is also not a paragraph<p>This is another paragraph</p>";
    return output;

if __name__ == "__main__":
    app.run()
