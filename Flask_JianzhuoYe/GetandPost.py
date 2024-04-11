'''
Name: Jianzhuo Ye
Start Date: 3/28/24
End Date: 3/31/24
Description: This program uses get and post to print an input on a separate HTML document
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('personalinfo.html')
    else:
        return GetInfo()

def GetInfo():
    global headings, data, taverage
    headings = ["PERIOD","TIME","CLASS","GRADE","TEACHER","ROOM #"]
    pd1 = request.form.get('txtpd1')
    pd2 = request.form.get('txtpd2')
    pd3 = request.form.get('txtpd3')
    pd4 = request.form.get('txtpd4')
    pd5 = request.form.get('txtpd5')
    pd6 = request.form.get('txtpd6')
    pd7 = request.form.get('txtpd7')
    pd8 = request.form.get('txtpd8')
    avg1 = request.form.get('txtpd1avg')
    avg2 = request.form.get('txtpd2avg')
    avg3 = request.form.get('txtpd3avg')
    avg4 = request.form.get('txtpd4avg')
    avg5 = request.form.get('txtpd5avg')
    avg6 = request.form.get('txtpd6avg')
    avg7 = request.form.get('txtpd7avg')
    avg8 = request.form.get('txtpd8avg')
    taverage = int(avg1) + int(avg2) + int(avg3) + int(avg4) + int(avg5) + int(avg6) + int(avg7) + int(avg8)
    taverage = taverage / 8;
    teach1 = request.form.get('txtpd1teacher')
    teach2 = request.form.get('txtpd2teacher')
    teach3 = request.form.get('txtpd3teacher')
    teach4 = request.form.get('txtpd4teacher')
    teach5 = request.form.get('txtpd5teacher')
    teach6 = request.form.get('txtpd6teacher')
    teach7 = request.form.get('txtpd7teacher')
    teach8 = request.form.get('txtpd8teacher')
    rm1 = request.form.get('txtpd1room')
    rm2 = request.form.get('txtpd2room')
    rm3 = request.form.get('txtpd3room')
    rm4 = request.form.get('txtpd4room')
    rm5 = request.form.get('txtpd5room')
    rm6 = request.form.get('txtpd6room')
    rm7 = request.form.get('txtpd7room')
    rm8 = request.form.get('txtpd8room')
    data = [
        ("1","08:00-08:45",pd1,avg1,teach1,rm1),
        ("2","08:47-09:32",pd2,avg2,teach2,rm2),
        ("3","09:35-10:20",pd3,avg3,teach3,rm3),
        ("4","10:23-11:08",pd4,avg4,teach4,rm4),
        ("5","11:11-11:56",pd5,avg5,teach5,rm5),
        ("6","11:59-12:44",pd6,avg6,teach6,rm6),
        ("7","12:47-01:32",pd7,avg7,teach7,rm7),
        ("8","01:35-02:20",pd8,avg8,teach8,rm8)
        ]
    return DisplayInfo()

def DisplayInfo():
    return render_template('personalinfooutput.html',headings=headings,data=data,totalaverage=taverage)

if __name__ == '__main__':
    app.run()
