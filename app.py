from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test():
    test_jpg = './static/image/test.jpg'
    return render_template('index.html', test_jpg = test_jpg)