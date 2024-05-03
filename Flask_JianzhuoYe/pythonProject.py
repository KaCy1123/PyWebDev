'''
Name: Jianzhuo Ye
Start Date: April 2nd
End Date: April 12th
'''
from flask import Flask, render_template, request, redirect
import math

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
    global FirstN,MiddleN,LastN,count
    FirstN = request.form.get('txtFname')
    LastN = request.form.get('txtLname')
    MiddleN = request.form.get('txtMname')
    SchoolN = request.form.get('txtSchool')
    Age = request.form.get('txtAge')
    count = 0
    return redirect('/page2')

@app.route('/page2',methods=["GET","POST"])
def mainCalc():
    global num1, num2, operator, dotCount, finaldollar, count
    if count == 0:
        num1 = '0'
        num2 = 0
        operator = ""
        dotCount = 0
        finaldollar = 0
        count += 1
    else:
        count = count
    if request.method == 'GET':
        return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,)
    else:
        return Calc()

def Calc():
    global pressed
    switcher = {
            '1': mathOne,
            '2': mathTwo,
            '3': mathThree,
            '4': mathFour,
            '5': mathFive,
            '6': mathSix,
            '7': mathSeven,
            '8': mathEight,
            '9': mathNine,
            '0': mathZero,
            'dot': mathDot,
            'sine': mathSin,
            'cosine': mathCos,
            'tangent': mathTan,
            'arcsine': mathaSin,
            'arccosine': mathaCos,
            'arctangent': mathaTan,
            'delete': mathDel,
            'clear': mathClear,
            'e': mathE,
            'root': mathRoot,
            'square': mathSquare,
            'percent': mathPercent,
            'absolute': mathAbs,
            'sign': mathSign,
            'add': mathAdd,
            'minus': mathSubtract,
            'times': mathMultiply,
            'divide': mathDivide,
            'exponent': mathExponent,
            'equals': mathEquals,
            'clear': mathClear,
            'error': error,
            'SUBMIT': Submit,
            'CALCULATE': Finance
            }
    
    pressed = request.form['button']
    return switcher.get(pressed, "error")()

def mathOne():
    global num1
    num1 += "1"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathTwo():
    global num1
    num1 += "2"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathThree():
    global num1
    num1 += "3"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathFour():
    global num1
    num1 += "4"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathFive():
    global num1
    num1 += "5"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathSix():
    global num1
    num1 += "6"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathSeven():
    global num1
    num1 += "7"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathEight():
    global num1
    num1 += "8"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathNine():
    global num1
    num1 += "9"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathZero():
    global num1
    num1 += "0"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathDot():
    global num1, dotCount
    if dotCount == 0:
        dotCount += 1
        num1 += "."
    else:
        dotCount = dotCount
        num1 = num1
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathSin():
    global num1
    num1 = float(num1)
    num1 = math.sin(num1) #returns the sine of a number
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathCos():
    global num1
    num1 = float(num1)
    num1 = math.cos(num1) #returns the cosine of a number
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathTan():
    global num1
    num1 = float(num1)
    num1 = math.tan(num1) #returns the tangent of a number
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathaSin():
    global num1
    num1 = float(num1)
    if num1 <= 1 and num1 >= -1:
        num1 = math.asin(num1) #returns the arcsine of a number
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathaCos():
    global num1
    num1 = float(num1)
    if num1 <= 1 and num1 >= -1:
        num1 = math.acos(num1) #returns the arccosine of a number
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathaTan():
    global num1
    limit1 = math.pi / 2
    limit2 = math.pi /2
    limit2 *= -1
    num1 = float(num1)
    if num1 <= limit1 and num1 >= limit2:
        num1 = math.atan(num1) #returns the arctangent of a number
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathDel():
    global num1
    num1 = num1[:-1]
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathClear():
    global num1, num2, operator
    num1 = "0"
    num2 = "0"
    operator = ""
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathE():
    global num1
    num1 = float(num1)
    if num1 == 0:
        num1 = math.e
    else:
        num1 = num1 * math.e #math.e = euler's number a.k.a. 2.7182...
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathRoot():
    global num1
    num1 = float(num1)
    num1 = math.sqrt(num1) #returns the square root of a number
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathSquare():
    global num1
    num1 = float(num1)
    num1 = num1 ** 2
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathPercent():
    global num1
    num1 = float(num1)
    num1 = num1 / 100
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathAbs():
    global num1
    num1 = float(num1)
    num1 = math.fabs(num1) #returns the absolute value of a number
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathSign():
    global num1
    num1 = float(num1)
    num1 = num1 * -1
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathAdd():
    global operator, num1, num2
    num1 = float(num1)
    if operator == "":
        operator = "+"
        num2 = num1
        num1 = "0"
        
    elif operator == "+":
        num1 = num2 + num1
        operator = ""
        
    elif operator == "-":
        num1 = num2 - num1
        operator = ""
        
    elif operator == "*":
        num1 = num2 * num1
        operator = ""
        
    elif operator == "/":
        num1 = num2 / num1
        operator = ""
        
    elif operator == "^":
        num1 = num2 ** num1
        operator = ""
        
    else:
        num1 = num1
        
    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathSubtract():
    global operator, num1, num2
    num1 = float(num1)
    if operator == "":
        operator = "-"
        num2 = num1
        num1 = "0"
        
    elif operator == "+":
        num1 = num2 + num1
        operator = ""
        
    elif operator == "-":
        num1 = num2 - num1
        operator = ""
        
    elif operator == "*":
        num1 = num2 * num1
        operator = ""
        
    elif operator == "/":
        num1 = num2 / num1
        operator = ""
        
    elif operator == "^":
        num1 = num2 ** num1
        operator = ""
        
    else:
        num1 = num1

    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathMultiply():
    global operator, num1, num2
    num1 = float(num1)
    if operator == "":
        operator = "*"
        num2 = num1
        num1 = "0"
        
    elif operator == "+":
        num1 = num2 + num1
        operator = ""
        
    elif operator == "-":
        num1 = num2 - num1
        operator = ""
        
    elif operator == "*":
        num1 = num2 * num1
        operator = ""
        
    elif operator == "/":
        num1 = num2 / num1
        operator = ""
        
    elif operator == "^":
        num1 = num2 ** num1
        operator = ""
               
    else:
        num1 = num1

    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathDivide():
    global operator, num1, num2
    num1 = float(num1)
    if operator == "":
        operator = "+"
        num2 = num1
        num1 = "0"
        
    elif operator == "+":
        num1 = num2 + num1
        operator = ""
        
    elif operator == "-":
        num1 = num2 - num1
        operator = ""
        
    elif operator == "*":
        num1 = num2 * num1
        operator = ""
        
    elif operator == "/":
        num1 = num2 / num1
        operator = ""
        
    elif operator == "^":
        num1 = num2 ** num1
        operator = ""
               
    else:
        num1 = num1

    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathExponent():
    global operator, num1, num2
    num1 = float(num1)
    if operator == "":
        operator = "^"
        num2 = num1
        num1 = "0"
        
    elif operator == "+":
        num1 = num2 + num1
        operator = ""
        
    elif operator == "-":
        num1 = num2 - num1
        operator = ""
        
    elif operator == "*":
        num1 = num2 * num1
        operator = ""
        
    elif operator == "/":
        num1 = num2 / num1
        operator = ""
        
    elif operator == "^":
        num1 = num2 ** num1
        operator = ""
               
    else:
        num1 = num1

    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def mathEquals():
    global operator, num1, num2
    num1 = float(num1)
    if operator == "":
        operator = ""
        num1 = num1
        num2 = ""
        
    elif operator == "+":
        num1 = num2 + num1
        operator = ""
        
    elif operator == "-":
        num1 = num2 - num1
        operator = ""
        
    elif operator == "*":
        num1 = num2 * num1
        operator = ""
        
    elif operator == "/":
        num1 = num2 / num1
        operator = ""
        
    elif operator == "^":
        num1 = num2 ** num1
        operator = ""
               
    else:
        num1 = num1

    num1 = str(num1)
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def error():
    global num1
    num1 = "0"
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)
    
def Submit():
    global score, solution1, solution2, solution3, input1, input2, input3
    solution1 = "9.5"
    solution2 = "3"
    solution3 = "-(cos(e)*tan(e)*sqrt(cot(e^2))*(ln(abs((cot(e^2)-1)*tan(x)+sqrt(1-cot(e^2))*sqrt(cot(e^2))))-"
    solution3 = solution3 + "ln(abs((cot(e^2)-1)*tan(x)-sqrt(1-cot(e^2))*sqrt(cot(e^2))))))/(2*sqrt(1-cot(e^2)))-cos(e)*tan(e)*x"
    input1 = request.form.get('txtQ1')
    input2 = request.form.get('txtQ2')
    input3 = request.form.get('txtQ3')
    score = 0
    if input1 == solution1:
        score += 1
        
    else:
        score = score
        
    if input2 == solution2:
        score += 1
        
    else:
        score = score
        
    if input3 == solution3:
        score += 1
        
    else:
        score = score
        
    return redirect('/page3')
    
def Finance():
    global finaldollar
    period = request.form.get('txtPeriod')
    init = request.form.get('txtInitial')
    rate = request.form.get('txtRate')
    period = float(period)
    init = float(init)
    rate = float(rate)
    rate = rate / 100
    finaldollar = 1 + rate
    finaldollar = finaldollar ** period
    finaldollar = init * finaldollar
    
    return render_template("projectcalc.html",Name=FirstN,Middle=MiddleN,Last=LastN,output=num1,FInterest=finaldollar)

@app.route('/page3', methods=['GET','POST'])
def mainQuiz():
    if request.method == "GET":
        return render_template("projectquiz.html",Name=FirstN,Middle=MiddleN,
                               Last=LastN,ans1=solution1,ans2=solution2,ans3=solution3,
                               inp1=input1,inp2=input2,inp3=input3,Qscore=score,lst="")
    else:
        return quizCalc()
    
def quizCalc():
    global Tlist
    Tsolution1 = "Berlin"
    Tsolution2 = "Anthony"
    Tsolution3 = "Michael Jackson"
    Tinput1 = request.form.get('txtT1')
    Tinput2 = request.form.get('txtT2')
    Tinput3 = request.form.get('txtT3')
    Tinput1 = str(Tinput1)
    Tinput2 = str(Tinput2)
    Tinput3 = str(Tinput3)
    score2 = 0
    if input1 == solution1:
        score2 += 1
        
    else:
        score2 = score2
        
    if input2 == solution2:
        score2 += 1
        
    else:
        score2 = score2
        
    if input3 == solution3:
        score2 += 1
        
    else:
        score2 = score2
    score2 = str(score2)
    score2 = "Total Score: " + score2
    Tsolution1 = "Solution: Berlin"
    Tsolution2 = "Solution: Anthony"
    Tsolution3 = "Solution: Michael Jackson"
    Tinput1 = "Input: " + Tinput1
    Tinput2 = "Input: " + Tinput2
    Tinput3 = "Input: " + Tinput3
    Tlist = [Tsolution1,Tinput1,Tsolution2,Tinput2,Tsolution3,Tinput3,score2]
    
    return render_template("projectquiz.html",Name=FirstN,Middle=MiddleN,
                               Last=LastN,ans1=solution1,ans2=solution2,ans3=solution3,
                               inp1=input1,inp2=input2,inp3=input3,Qscore=score,lst=Tlist)
if __name__ == "__main__":
    app.run()
