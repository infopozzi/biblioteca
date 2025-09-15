from flask import Blueprint, render_template, request, redirect, jsonify
from Repositorio.Editora import Editora

editora_route = Blueprint('editora', __name__)

@editora_route.route('/')
def listar():    
    return render_template('./Editora/index.html', lista = Editora.listar())


@editora_route.route('/cadastro')
def cadastro():
    item = Editora.novo()
    return render_template('./Editora/cadastro.html', item = item)


@editora_route.route('/cadastro/<int:id>')
def obter(id):
    item = Editora.obter(id)
    return render_template('./Editora/cadastro.html', item = item)


@editora_route.route('/cadastro', methods=['POST'])
def salvar():
    Editora.salvar(int(request.form['id']), request.form['nome'])    
    return redirect('/editora')


@editora_route.route('/excluirAjax', methods=['POST'])
def excluirAjax():
    id = int(request.form.get('id', 0))
    if (id > 0):
        Editora.excluir(id)
    return jsonify({'status': 'success',
                    'message': 'Editora excluído com sucesso!'
                    }), 200
