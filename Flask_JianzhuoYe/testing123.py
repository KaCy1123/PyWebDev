from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('testing.html')


@app.route('/test')
def test():
    return "we ball"


if __name__ == "__main__":
    app.run()
