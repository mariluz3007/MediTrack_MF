from flask import Blueprint, render_template
from app import db
from app.models import Medicamento

main = Blueprint("main", __name__)

#poner los decoradores de @app.route o @mai.route para las rutas de las paginas web

#Ruta del home/pagina principal
@main.route("/")
def dashboard():
    return render_template("dashboard.html")

# Ruta para consultar los detalles de los medicamentos
@main.route("/detallesMedicamentos/<int:medicamento_id>")
def detallesMeds(medicamento_id):
    medicamento = db.get_or_404(Medicamento, medicamento_id)
    return render_template(
        "medicamentos/consultas/detailsMeds.html",
        medicamento=medicamento,
    )

# Ruta para consultar/buscar y listar medicamentos    
@main.route("/listarMedicamentos")
def listarMeds():
    medicamentos = db.session.scalars(
        db.select(Medicamento).order_by(Medicamento.nombre)
    ).all()
    return render_template(
        "medicamentos/consultas/buscarMeds.html",
        medicamentos=medicamentos,
    )

#Errores (manejo de errores en la pagina)
@main.app_errorhandler(404)
def not_found(error):
    return render_template("errores/404.html"), 404


@main.app_errorhandler(500)
def internal_error(error):
    return render_template("errores/500.html"), 500
