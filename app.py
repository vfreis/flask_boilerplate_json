from flask import request, jsonify
from app import create_app
from models import Usuario, Agenda


app = create_app()

# @app.route("/agenda/<int:id>", methods=['GET', 'POST', 'PUT'])
# def users(id):
#     return agenda_por_userid(id)

# @app.route("/usuarios", methods=['GET'])
# def get_users():
#     return get_usuarios()


@app.route('/usuario', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    usuarios_dict = [usuario.to_dict() for usuario in usuarios]
    return jsonify(usuarios_dict)

@app.route('/usuario/<int:id>', methods=['GET'])
def buscar_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()
    if usuario:
        return jsonify(usuario.to_dict())
    else:
        return jsonify({"message": "Usuário não encontrado"}), 404

@app.route('/usuario', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    novo_usuario = Usuario(
        nome=data['nome'],
        data_nascimento=datetime.fromisoformat(data['data_nascimento']) if data['data_nascimento'] else None,
        sexo=data['sexo'],
        email=data['email'],
        telefone=data['telefone'],
        senha=data['senha']
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify(novo_usuario.to_dict()), 201

@app.route('/usuario/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()
    if not usuario:
        return jsonify({"message": "Usuário não encontrado"}), 404
    data = request.get_json()
    usuario.nome = data['nome']
    usuario.data_nascimento = datetime.fromisoformat(data['data_nascimento']) if data['data_nascimento'] else None
    usuario.sexo = data['sexo']
    usuario.email = data['email']
    usuario.telefone = data['telefone']
    usuario.senha = data['senha']
    db.session.commit()
    return jsonify(usuario.to_dict())

@app.route('/usuario/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()
    if not usuario:
        return jsonify({"message": "Usuário não encontrado"}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"message": "Usuário excluído com sucesso"}), 200

# Rotas para a classe Agenda
@app.route('/agenda', methods=['GET'])
def listar_agendas():
    agendas = Agenda.query.all()
    agendas_dict = [agenda.to_dict() for agenda in agendas]
    return jsonify(agendas_dict)

@app.route('/agenda/<int:id>', methods=['GET'])
def buscar_agenda(id):
    agenda = Agenda.query.filter_by(id_agenda=id).first()
    if agenda:
        return jsonify(agenda.to_dict())
    else:
        return jsonify({"message": "Agenda não encontrada"}), 404

@app.route('/agenda', methods=['POST'])
def cadastrar_agenda():
    data = request.get_json()
    usuario = Usuario.query.filter_by(id=data['id_usuario']).first()
    nova_agenda = Agenda(
        estado=data['estado'],
        especialidade=data['especialidade'],
        regiao=data['regiao'],
        unidade=data['unidade'],
        profissional=data['profissional'],
        data=datetime.fromisoformat(data['data']),
        hora=datetime.strptime(data['hora'], '%H:%M:%S').time(),
        usuario=usuario
    )
    db.session.add(nova_agenda)
    db.session.commit()
    return jsonify(nova_agenda.to_dict()), 201

# Rotas para a classe Agenda
@app.route('/agenda', methods=['GET'])
def listar_agendas():
    agendas = Agenda.query.all()
    agendas_dict = [agenda.to_dict() for agenda in agendas]
    return jsonify(agendas_dict)

@app.route('/agenda/<int:id>', methods=['GET'])
def buscar_agenda(id):
    agenda = Agenda.query.filter_by(id_agenda=id).first()
    if agenda:
        return jsonify(agenda.to_dict())
    else:
        return jsonify({"message": "Agenda não encontrada"}), 404

@app.route('/agenda', methods=['POST'])
def cadastrar_agenda():
    data = request.get_json()
    usuario = Usuario.query.filter_by(id=data['id_usuario']).first()
    nova_agenda = Agenda(
        estado=data['estado'],
        especialidade=data['especialidade'],
        regiao=data['regiao'],
        unidade=data['unidade'],
        profissional=data['profissional'],
        data=datetime.fromisoformat(data['data']),
        hora=datetime.strptime(data['hora'], '%H:%M:%S').time(),
        usuario=usuario
    )
    db.session.add(nova_agenda)
    db.session.commit()
    return jsonify(nova_agenda.to_dict()), 201

@app.route('/agenda/<int:id>', methods=['PUT'])
def atualizar_agenda(id):
    agenda = Agenda.query.filter_by(id_agenda=id).first()
    if not agenda:
        return jsonify({"message": "Agenda não encontrada"}), 404
    data = request.get_json()
    agenda.estado = data['estado']
    agenda.especialidade = data['especialidade']
    agenda.regiao = data['regiao']
    agenda.unidade = data['unidade']
    agenda.profissional = data['profissional']
    agenda.data = datetime.fromisoformat(data['data'])
    agenda.hora = datetime.strptime(data['hora'], '%H:%M:%S').time()
    db.session.commit()
    return jsonify(agenda.to_dict())

@app.route('/agenda/<int:id>', methods=['DELETE'])
def excluir_agenda(id):
    agenda = Agenda.query.filter_by(id_agenda=id).first()
    if not agenda:
        return jsonify({"message": "Agenda não encontrada"}), 404
    db.session.delete(agenda)
    db.session.commit()
    return jsonify({"message": "Agenda excluída com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug = True)