from recetas_app import app
from recetas_app.controladores import controlador_usuarios, controlador_recetas

if __name__ == "__main__":
    app.run( debug = True )