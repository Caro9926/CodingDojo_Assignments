from flask import Flask # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/', methods=['GET'])          
def holaMundo():
    return "Hola Mundo" # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/Dojo', methods=['GET'])          
def dojoPrint():
    return "Dojo!" 

@app.route('/say/<string:name>') 
def hola(name):            
    print(name)
    return "¡Hola, " + name + "!"


@app.route('/repeat/<string:word>/<int:number>') 
def repeatmany(word, number):
    return f"{word * number}"

   


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

