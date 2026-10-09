"""Modelos de datos de la DB de Meditrack."""

from datetime import datetime, timezone

from sqlalchemy import Boolean, Date, DateTime, Float, Integer, String, Text

from app import db


class Medicamento(db.Model):
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(100), nullable=False)
    descripcion = db.Column(Text, nullable=False)
    laboratorio = db.Column(String(100), nullable=False)
    precio = db.Column(Float, nullable=False)
    stock = db.Column(Integer, nullable=False)
    fecha_vencimiento = db.Column(Date, nullable=False)
    requiere_receta = db.Column(Boolean, nullable=False)
    fecha_registro = db.Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )