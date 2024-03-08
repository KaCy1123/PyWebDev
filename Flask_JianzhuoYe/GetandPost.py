'''
Name: Jianzhuo Ye
Start Date: 3/7/24
End Date: 3/8/24
Description: This program uses get and post to print an input on a separate HTML document
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('personinfo.html')
    else:
        GetInfo()
        return render_template('personinfo.html')

def GetInfo():
    global output
    name = request.form.get('txtname')
    email = request.form.get('txtemail')
    output = "Hello " + name + ". Thank you for your email " + email

@app.route('/output')
def output():
    
    return "<h1>" + output + "</h1>"

if __name__ == '__main__':
    app.run()
