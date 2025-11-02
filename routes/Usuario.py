from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from Repositorio.Usuario import Usuario, UsuarioNaoEncontrado

usuario_route = Blueprint('usuario', __name__)

# --- Rota para listagem de usuários ---
@usuario_route.route('/')
def index():
    lista_usuarios = Usuario.listar()
    return render_template('usuario/index.html', lista=lista_usuarios)


# --- Rota para cadastro e edição ---
@usuario_route.route('/cadastro', methods=['GET', 'POST'])
@usuario_route.route('/cadastro/<int:id>', methods=['GET', 'POST'])
def cadastro(id=0):
    if request.method == 'POST':
        # Pega o ID do formulário
        id_form = request.form.get('id', type=int)

        # Busca ou cria novo usuário
        usuario = Usuario.obter(id_form) if id_form and id_form > 0 else Usuario()

        # Pega os campos do formulário
        usuario.tipo = request.form.get('tipo', type=int)
        usuario.nome = request.form.get('nome')
        usuario.cpf = request.form.get('cpf')
        usuario.email = request.form.get('email')
        usuario.telefone = request.form.get('telefone')
        usuario.status = request.form.get('status', type=int)
        usuario.observacao = request.form.get('observacao')

        # Validação simples
        if not usuario.nome or not usuario.cpf or not usuario.email:
            return "Erro: Nome, CPF e E-mail são obrigatórios.", 400

        # Salva no banco
        try:
            usuario.salvar()
            return redirect(url_for('usuario.index'))
        except Exception as e:
            return f"Erro ao salvar usuário: {e}", 500

    
    # Se for GET
    usuario = Usuario.novo() if id == 0 else Usuario.obter(id)
    return render_template('usuario/cadastro.html', usuario=usuario)


# --- Rota para exclusão via AJAX ---
@usuario_route.route('/excluirAjax', methods=['POST'])
def excluir_ajax():
    id_usuario = request.form.get('id', type=int)
    if not id_usuario:
        return jsonify({'status': 'ERROR', 'message': 'ID inválido.'}), 400

    try:
        Usuario.excluir(id_usuario)
        return jsonify({'status': 'OK', 'message': 'Usuário excluído com sucesso.'})
    except UsuarioNaoEncontrado as e:
        return jsonify({'status': 'ERROR', 'message': str(e)}), 404
    except Exception as e:
        return jsonify({'status': 'ERROR', 'message': f'Erro ao excluir: {str(e)}'}), 500
