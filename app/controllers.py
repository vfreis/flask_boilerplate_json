from flask import jsonify, json
from sqlalchemy import update
from .models import Agenda, Usuario
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

