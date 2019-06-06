from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template("result.html")
    if request.method == 'POST':
        sizeOfStartingPopulation = request.form['sizeOfPopulation']
        runMpiApp(sizeOfStartingPopulation)
        return render_template("result.html")
    return render_template("result.html")


def runMpiApp(sizeOfStartingPopulation):
    os.system("mpiexec -np 3 python main.py")
    # os.system("mpiexec -np 3 python main.py " + sizeOfStartingPopulation)

if __name__ == '__main__':
    app.run()
