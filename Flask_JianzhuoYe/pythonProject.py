from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main():
    if request.method == 'GET':
        return render_template('projectindex.html')
    else:
        return GetLogin()

def GetLogin():
    global user, pw
    user = request.form.get('txtUser')
    pw = request.form.get('txtPassword')
    if (user == 'jianzhuoy') & (pw == 'yjz1123'):
        return redirect('/page1')
    else:
        msg = "Incorrect username or password"
        return render_template('projectindex.html',incorrect=msg)
    
@app.route('/page1',methods=["GET","POST"])
def mainPersonal():
    if request.method == 'GET':
        return render_template('projectpersonalinfo.html',user=user)
    else:
        return GetPersonal()

def GetPersonal():
    global FirstN,MiddleN,LastN
    FirstN = request.form.get('txtFname')
    LastN = request.form.get('txtLname')
    MiddleN = request.form.get('txtMname')
    SchoolN = request.form.get('txtSchool')
    Age = request.form.get('txtAge')
    return redirect('/page2')

@app.route('/page2',methods=["GET","POST"])
def mainCalc():
    global num1, num2
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN)
    num1 = ""
    num2 = ""
    if request.method == 'GET':
        return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN)
    else:
        return Calc()

def Calc():
    global pressed
    switcher:{
            1: mathOne(),
            2: mathTwo(),
            3: mathThree(),
            4: mathFour(),
            5: mathFive(),
            6: mathSix(),
            7: mathSeven(),
            8: mathEight(),
            9: mathNine(),
            add: mathAdd(),
            minus: mathSubtract(),
            times: mathMultiply(),
            divide: mathDivide(),
            error: error()
            }
    pressed = request.form['button']
    return switch.get(pressed, "error")

def mathOne():
    global num1
    num1 += "1"

    
if __name__ == "__main__":
    app.run()
