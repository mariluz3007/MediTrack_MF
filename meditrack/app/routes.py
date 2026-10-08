from flask import Blueprint, render_template

main = Blueprint("main", __name__)

#poner los decoradores de @app.route o @mai.route para las rutas de las paginas web

#Ruta del home/pagina principal
@main.route("/")
def dashboard():
    return render_template("base.html") #Aclarar si aqui ira base.html o dashboard.html

# Ruta para consultar los detalles de los medicamentos
@main.route("/detallesMedicamentos")
def detallesMeds():
    return render_template("detailsMeds.html")

# Ruta para consultar/buscar y listar medicamentos    
@main.route("/listarMedicamentos")
def listarMeds():
    return render_template("buscarMeds.html")

#Errores (manejo de errores en la pagina)
@main.app_errorhandler(404)
def not_found(error):
    return render_template("errores/404.html"), 404


@main.app_errorhandler(500)
def internal_error(error):
    return render_template("errores/500.html"), 500
