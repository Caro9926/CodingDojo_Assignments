from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def chess_1():
    return render_template("index.html", x=8, y=8, color1="red", color2="black")


@app.route('/<int:row>')
def chess_2(row):
    return render_template("index.html",x=row,y=8,color1='red',color2="black")

@app.route('/<int:row>/<int:col>')
def chess_3(row,col):
    return render_template("index.html",x=row, y=col,color1='red',color2="black")

@app.route('/<int:row>/<int:col>/<string:colour>')
def chess_4(row,col, colour):
    return render_template("index.html",x=row,y=col,color1=colour,color2="black")




if __name__=="__main__":
    app.run(debug=True)