from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key="ContadorCore"


@app.route('/')
def contador_uno():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template("index.html")

@app.route('/doble')
def contador_dos():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 2
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


@app.route('/reset2')
def reset2():
    session.clear()
    return redirect('/doble')


if __name__ == "__main__":
    app.run( debug = True )


   




