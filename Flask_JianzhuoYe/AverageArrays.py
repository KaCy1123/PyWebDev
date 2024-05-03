'''
Name: Jianzhuo Ye
Start Date: April 17th, 2024
End Date: TBD
Description: This program will receive the user's classes and grades and
             produce a transcript with an overall average
'''
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('transcriptGet.html');
    else:
        return GetGrades();

def GetGrades():
    global headers, outputarray
    cls1 = request.form.get('txtClass1');
    cls2 = request.form.get('txtClass2');
    cls3 = request.form.get('txtClass3');
    cls4 = request.form.get('txtClass4');
    cls5 = request.form.get('txtClass5');
    cls6 = request.form.get('txtClass6');
    cls7 = request.form.get('txtClass7');
    cls8 = request.form.get('txtClass8');
    
    avg1 = float(request.form.get('txtAverage1'));
    avg2 = float(request.form.get('txtAverage2'));
    avg3 = float(request.form.get('txtAverage3'));
    avg4 = float(request.form.get('txtAverage4'));
    avg5 = float(request.form.get('txtAverage5'));
    avg6 = float(request.form.get('txtAverage6'));
    avg7 = float(request.form.get('txtAverage7'));
    avg8 = float(request.form.get('txtAverage8'));
    tavg = avg1 + avg2 + avg3 + avg4 + avg5 + avg6 + avg7 + avg8
    tavg = tavg / 8
    
    gpa = tavg * 4
    gpa = gpa / 100

    match tavg:
        case tavg if tavg < 65:
            letter = 'F'
        case tavg if tavg >= 65 and if tavg < 70:
            letter = 'D'
        case tavg if tavg >= 70 and if tavg < 80:
            letter = 'C'
        case tavg if tavg >= 80 and if tavg < 90:
            letter = 'B'
        case tavg if tavg >= 90:
            letter = 'A'
        
    headers = ['Class','Grade','Scale','Average']
    outputarray = ([cls1,avg1,'Average',tavg],[cls2,avg2,'GPA',gpa],
                   [cls3,avg3,'Letter',letter],[cls4,avg4],[cls5,avg5],
                   [cls6,avg6],[cls7,avg7],[cls8,avg8])

    return redirect('/transcript')

@app.route('/transcript',methods=['GET','POST'])
def transMain():
    return render_template('transcriptPost.html',headings=headers,data=outputarray);


if __name__ == "__main__":
    app.run()
