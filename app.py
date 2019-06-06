from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template("result.html")
    if request.method == 'POST':
        sizeOfPopulation = request.form['sizeOfPopulation']
        return render_template("result.html")
    return render_template("result.html")


if __name__ == '__main__':
    app.run()
