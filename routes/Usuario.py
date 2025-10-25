from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from Repositorio.Usuario import Usuario, UsuarioNaoEncontrado

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/usuario')
def index():
    lista = Usuario.listar()
    return render_template('usuario/index.html', lista=lista)

@usuario_route.route('/usuario/cadastro', methods=['GET'])
@usuario_route.route('/usuario/cadastro/<int:id>', methods=['GET'])
def cadastro(id=None):
    if id:
        usuario = Usuario.obter(id)
    else:
        usuario = Usuario.novo()
    return render_template('usuario/cadastro.html', usuario=usuario)

@usuario_route.route('/usuario/salvar', methods=['POST'])
def salvar():
    f = request.form
    id = f.get('id')
    if id and id != '0':
        usuario = Usuario.obter(int(id))
    else:
        usuario = Usuario.novo()

    # mapear campos do formulário para o modelo
    usuario.idExemplar = int(f.get('idExemplar')) if f.get('idExemplar') else None
    usuario.tipo = int(f.get('tipo')) if f.get('tipo') else 0
    usuario.nome = f.get('nome', '').strip()
    usuario.cpf = f.get('cpf', '').strip()
    usuario.email = f.get('email', '').strip()
    usuario.telefone = f.get('telefone', '').strip()
    usuario.endereco = f.get('endereco', '').strip()
    usuario.status = int(f.get('status')) if f.get('status') else 0
    usuario.observacao = f.get('observacao', '').strip()

    usuario.salvar()
    return redirect(url_for('usuario.index'))

@usuario_route.route('/usuario/excluir/<int:id>', methods=['POST', 'DELETE'])
def excluir(id):
    try:
        Usuario.excluir(id)
        if request.is_json or request.method == 'DELETE':
            return jsonify({'status': 'ok'})
        return redirect(url_for('usuario.index'))
    except UsuarioNaoEncontrado as e:
        if request.is_json or request.method == 'DELETE':
            return jsonify({'status': 'error', 'message': str(e)}), 404
        return redirect(url_for('usuario.index'))