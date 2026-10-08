"""Modelos de datos de la DB de Meditrack."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime

base = declarative_base()

class Medicamento(base):
    __tablename__ = 'medicamentos'
    # ID = 
    # nombre = 
    
    pass