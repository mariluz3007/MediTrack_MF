#Punto de entrada para iniciar la app.
from app import create_app

app = create_app()

#poner los decoradores de @app.route para las rutas de las paginas web
#

if __name__ == "__main__":
    app.run(debug=True)
