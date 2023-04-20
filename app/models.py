from . import db
import datetime
from dataclasses import dataclass

# from sqlalchemy import func
@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(150))
    data_nascimento = db.Column(db.DateTime)
    sexo = db.Column(db.String(10))
    email = db.Column(db.String(150))
    telefone = db.Column(db.String(150))
    senha = db.Column(db.String(150))
    agenda = db.relationship('Agenda', backref='usuario', lazy=True)
    

@dataclass
class Agenda(db.Model):
    __tablename__ = 'agenda'
    id_agenda = db.Column(db.Integer, primary_key = True, autoincrement = True)
    estado = db.Column(db.String(50))
    especialidade = db.Column(db.String(100))
    regiao = db.Column(db.String(20))
    unidade = db.Column(db.String(100))
    profissional = db.Column(db.String(50))
    data = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    hora = db.Column(db.Time)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))

