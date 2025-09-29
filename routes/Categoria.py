from flask import Blueprint, render_template, request, redirect, jsonify
from Repositorio.Categoria import Categoria

categoria_route = Blueprint('categoria', __name__)


@categoria_route.route('/')
def listar():
    return render_template('./Categoria/index.html', lista=Categoria.listar())


@categoria_route.route('/cadastro')
def cadastro():
    item = Categoria.novo()
    return render_template('./Categoria/cadastro.html', item=item)


@categoria_route.route('/cadastro/<int:id>')
def obter(id):
    item = Categoria.obter(id)
    return render_template('./Categoria/cadastro.html', item=item)


@categoria_route.route('/cadastro', methods=['POST'])
def salvar():
    Categoria.salvar(int(request.form['id']), request.form['nome'])
    return redirect('/categoria')


@categoria_route.route('/excluirAjax', methods=['POST'])
def excluirAjax():
    id = int(request.form.get('id', 0))
    if (id > 0):
        Categoria.excluir(id)
    return jsonify({'status': 'success',
                    'message': 'categoria excluída com sucesso!'
                    }), 200


@categoria_route.route('/cadastroAjax', methods=['POST'])
def cadastro_ajax():
    try:
        Categoria.salvar(int(request.form.get('id', 0)), request.form.get('nome'))
        lista_categorias = Categoria.listar()
        categorias_json = [cat.to_dict() for cat in lista_categorias]

        return jsonify({
            'status': 'success',
            'message': 'Categoria salva com sucesso!',
            'categorias': categorias_json
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400