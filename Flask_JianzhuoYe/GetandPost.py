'''
Name: Jianzhuo Ye
Start Date: 3/7/24
End Date: 3/8/24
Description: This program uses get and post to print an input on a separate HTML document
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('personinfo.html')
    else:
        GetInfo()
        return render_template('personinfooutput.html')
        return redirect(url_for("out", output1 = output))

def GetInfo():
    global output
    name = request.form.get('txtname')
    email = request.form.get('txtemail')
    output = "Hello " + name + ". Thank you for your email " + email
    
@app.route('/<output1>')
def out(output1):
    return f"{output1}"
    
if __name__ == '__main__':
    app.run()
