from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import Medicamento
from .forms import MedicamentoForm

gestion_bp = Blueprint(
    "gestion",
    __name__,
    url_prefix="/medicamentos"
)


@gestion_bp.route("/nuevo", methods=["GET", "POST"])
def crear_medicamento():
    form = MedicamentoForm()

    if form.validate_on_submit():
        medicamento = Medicamento(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            laboratorio=form.laboratorio.data,
            precio=form.precio.data,
            stock=form.stock.data,
            fecha_vencimiento=form.fecha_vencimiento.data,
            requiere_receta=form.requiere_receta.data
        )

        db.session.add(medicamento)
        db.session.commit()

        flash("Medicamento creado correctamente.", "success")

        return redirect(url_for("consultas.lista_medicamentos"))

    return render_template(
        "gestion/formulario.html",
        form=form,
        titulo="Nuevo medicamento"
    )


@gestion_bp.route("/<int:id>/editar", methods=["GET", "POST"])
def editar_medicamento(id):
    medicamento = db.get_or_404(Medicamento, id)
    form = MedicamentoForm(obj=medicamento)

    if form.validate_on_submit():
        medicamento.nombre = form.nombre.data
        medicamento.descripcion = form.descripcion.data
        medicamento.laboratorio = form.laboratorio.data
        medicamento.precio = form.precio.data
        medicamento.stock = form.stock.data
        medicamento.fecha_vencimiento = form.fecha_vencimiento.data
        medicamento.requiere_receta = form.requiere_receta.data

        db.session.commit()

        flash("Medicamento actualizado correctamente.", "success")

        return redirect(url_for("consultas.lista_medicamentos"))

    return render_template(
        "gestion/formulario.html",
        form=form,
        titulo="Editar medicamento"
    )


@gestion_bp.route("/<int:id>/eliminar", methods=["POST"])
def eliminar_medicamento(id):
    medicamento = db.get_or_404(Medicamento, id)

    db.session.delete(medicamento)
    db.session.commit()

    flash("Medicamento eliminado correctamente.", "success")

    return redirect(url_for("consultas.lista_medicamentos"))