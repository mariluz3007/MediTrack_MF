from datetime import date

from app import db
from app.models import Medicamento


def test_lista_muestra_mensaje_si_no_hay_medicamentos(client):
    response = client.get("/listarMedicamentos")

    assert response.status_code == 200
    assert "Aún no hay medicamentos registrados.".encode() in response.data


def test_lista_y_detalle_muestran_medicamento(client, app):
    with app.app_context():
        medicamento = Medicamento(
            nombre="Paracetamol",
            descripcion="Analgésico",
            laboratorio="Laboratorio Uno",
            precio=12.5,
            stock=20,
            fecha_vencimiento=date(2027, 5, 1),
            requiere_receta=False,
        )
        db.session.add(medicamento)
        db.session.commit()
        medicamento_id = medicamento.id

    lista = client.get("/listarMedicamentos")
    detalle = client.get(f"/detallesMedicamentos/{medicamento_id}")

    assert lista.status_code == 200
    assert b"Paracetamol" in lista.data
    assert f"/detallesMedicamentos/{medicamento_id}".encode() in lista.data
    assert detalle.status_code == 200
    assert b"Analg\xc3\xa9sico" in detalle.data
    assert b"Laboratorio Uno" in detalle.data
    assert b"20" in detalle.data


def test_detalle_inexistente_devuelve_404(client):
    response = client.get("/detallesMedicamentos/999")

    assert response.status_code == 404