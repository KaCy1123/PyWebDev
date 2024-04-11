'''
Name: Jianzhuo Ye
Start Date: 3/27/24
End Date: 3/28/24
Description: This tutorial demonstrates the use of a for loop
             and includes errors to be fixed
'''
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])

def main():
    if request.method == 'GET': #'Post' changed to 'GET'
        return MainScreen() #added return
    else:
        return render_template("forloopintro.html") #"indexfor.html" change to "forloopintro"
    
def MainScreen():
    mylist = []
    mylist = ["Math","Science","English","History","Software Engineering"]
    mylistlen = len(mylist)
    return render_template("forloopintro.html",mylistlen=mylistlen,mylist=mylist)

if __name__ == "__main__":
    app.run()
    
