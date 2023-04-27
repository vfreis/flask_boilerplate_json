from flask import jsonify, json
from sqlalchemy import update
from ..models import Agenda, Usuario
from datetime import datetime, time
from . import db

import json

def agenda_por_userid(id_usuario):
    # Executa a consulta usando o SQLAlchemy
    agenda = Agenda.query.filter_by(id_usuario=id_usuario).all()

    # Serializa o resultado em formato JSON
    agenda_json = json.dumps([{
        'id_agenda': a.id_agenda,
        'estado': a.estado,
        'especialidade': a.especialidade,
        'regiao': a.regiao,
        'unidade': a.unidade,
        'profissional': a.profissional,
        'data': str(a.data),
        'hora': str(a.hora),
        'id_usuario': a.id_usuario
    } for a in agenda])

    # Retorna o resultado em formato JSON
    return agenda_json

def login(_email,_senha):
    usuario_var = Usuario.query.filter_by(email = _email).first()
    return True if usuario_var and usuario_var.senha == _senha else False

def get_usuarios():
    users = Usuario.query.all()
    users_json = jsonify([user.to_dict() for user in users])
    return users_json

def delete_usuario(_id):
    usuario_var = Usuario.query.filter_by(id=_id).first()
    db.session.delete(usuario_var)
    db.session.commit()
    return usuario_var.nome + ' deletado'

def update_user(_id, _nome, _data_nascimento, _sexo, _email, _telefone, _senha):
    usuario = Usuario.query.get(_id)
    usuario.nome = _nome
    usuario.data_nascimento = _data_nascimento
    usuario.sexo = _sexo
    usuario.email = _email
    usuario.telefone = _telefone
    usuario.senha = _senha
    db.session.commit()
    return usuario.nome + ' atualizado'