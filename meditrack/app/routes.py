#Ojo: invetsigar que hace y como funciona la funcion Blueprint de Flask 
from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def dashboard():
    return render_template("dashboard.html")


@main.app_errorhandler(404)
def not_found(error):
    return render_template("errores/404.html"), 404


@main.app_errorhandler(500)
def internal_error(error):
    return render_template("errores/500.html"), 500
