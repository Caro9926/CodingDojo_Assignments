#Parte de este código fue adapatado de Coding Dojo
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/play')
def nivel_uno():
    return render_template("index.html",num=3,color="blue")

@app.route('/play/<int:num>')
def nivel_dos(num):
    return render_template("index.html", num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def nivel_tres(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)