from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, DateField, BooleanField, SubmitField

from wtforms.validators import DataRequired, NumberRange, Length

class MedicamentoForm(FlaskForm):
    nombre = StringField(
        "Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(max=100)
        ]
    )

    descripcion = TextAreaField(
        "Descripción",
        validators=[
            DataRequired(message="La descripción es obligatoria.")
        ]
    )

    laboratorio = StringField(
        "Laboratorio",
        validators=[
            DataRequired(message="El laboratorio es obligatorio."),
            Length(max=100)
        ]
    )

    precio = FloatField(
        "Precio",
        validators=[
            DataRequired(message="El precio es obligatorio."),
            NumberRange(
                min=0,
                message="El precio no puede ser negativo."
            )
        ]
    )

    stock = IntegerField(
        "Stock",
        validators=[
            DataRequired(message="El stock es obligatorio."),
            NumberRange(
                min=0,
                message="El stock no puede ser negativo."
            )
        ]
    )

    fecha_vencimiento = DateField(
        "Fecha de vencimiento",
        validators=[
            DataRequired(
                message="La fecha de vencimiento es obligatoria."
            )
        ],
        format="%d-%m-%Y"
    )

    requiere_receta = BooleanField(
        "Requiere receta"
    )

    submit = SubmitField("Guardar medicamento")