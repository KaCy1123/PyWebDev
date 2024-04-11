from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return calc()

def calc():
    global total
    num1 = request.form.get('txtnum1')
    num2 = request.form.get('txtnum2')
    ttl = int(num1) + int(num2)
    return render_template('page2.html',total = ttl)

if __name__ == "__main__":
    app.run()
