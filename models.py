from .app import db
import datetime
from dataclasses import dataclass

# from sqlalchemy import func
@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    data_nascimento = db.Column(db.DateTime)
    sexo = db.Column(db.String(10))
    email = db.Column(db.String(150))
    telefone = db.Column(db.String(150))
    senha = db.Column(db.String(150))
    agendas = db.relationship('Agenda', backref='usuario', lazy=True)

    def __init__(self, nome, data_nascimento, sexo, email, telefone, senha):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.senha = senha

    def __repr__(self):
        return '<Usuario %r>' % self.nome

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.isoformat() if self.data_nascimento else None,
            "sexo": self.sexo,
            "email": self.email,
            "telefone": self.telefone,
            "senha": self.senha
        }

# Classe Agenda
class Agenda(db.Model):
    __tablename__ = 'agenda'
    id_agenda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estado = db.Column(db.String(50))
    especialidade = db.Column(db.String(100))
    regiao = db.Column(db.String(20))
    unidade = db.Column(db.String(100))
    profissional = db.Column(db.String(50))
    data = db.Column(db.DateTime(timezone=True))
    hora = db.Column(db.Time)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    def __init__(self, estado, especialidade, regiao, unidade, profissional, data, hora, usuario):
        self.estado = estado
        self.especialidade = especialidade
        self.regiao = regiao
        self.unidade = unidade
        self.profissional = profissional
        self.data = data
        self.hora = hora
        self.usuario = usuario

    def __repr__(self):
        return '<Agenda %r>' % self.id_agenda

    def to_dict(self):
        return {
            "id_agenda": self.id_agenda,
            "estado": self.estado,
            "especialidade": self.especialidade,
            "regiao": self.regiao,
            "unidade": self.unidade,
            "profissional": self.profissional,
            "data": self.data.isoformat(),
            "hora": self.hora.strftime('%H:%M:%S'),
            "id_usuario": self.id_usuario
        }