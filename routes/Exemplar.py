from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from Repositorio.Exemplar import Exemplar
from Repositorio.Publicacao import Publicacao

exemplar_route = Blueprint('exemplar', __name__)

@exemplar_route.route('/')
def index():
    lista_exemplares = Exemplar.listar()
    return render_template('exemplar/index.html', lista=lista_exemplares)

@exemplar_route.route('/cadastro', methods=['GET', 'POST'])
@exemplar_route.route('/cadastro/<int:id>', methods=['GET', 'POST'])
def cadastro(id=0):
    if request.method == 'POST':
        id_form = request.form.get('id', 0, type=int)
        item = Exemplar.obter(id_form) if id_form > 0 else Exemplar()

        id_publicacao = request.form.get('idPublicacao')
        localizacao = request.form.get('localizacao')
        status = request.form.get('status', type=int)
        condicoes = request.form.get('condicoes', type=int)
        
        if not id_publicacao or not localizacao:
            return "Erro: Publicação e Localização são campos obrigatórios.", 400

        item.idPublicacao = int(id_publicacao)
        item.localizacao = localizacao
        item.status = status
        item.condicoes = condicoes

        item.salvar()
        return redirect(url_for('exemplar.index'))

    item = Exemplar.novo() if id == 0 else Exemplar.obter(id)
    publicacoes = Publicacao.listar()
    return render_template('exemplar/cadastro.html', item=item, publicacoes=publicacoes)

@exemplar_route.route('/excluirAjax', methods=['POST'])
def excluir_ajax():
    try:
        id_ex = request.form.get('id')
        Exemplar.excluir(id_ex)
        return jsonify({'status': 'OK', 'message': 'Exemplar excluído com sucesso.'})
    except Exception as e:
        return jsonify({'status': 'ERROR', 'message': str(e)}), 400
