from flask import Blueprint, render_template, request, redirect, jsonify
from Repositorio.Autor import Autor

autor_route = Blueprint('autor', __name__)


@autor_route.route('/')
def listar():
    return render_template('./Autor/index.html', lista=Autor.listar())


@autor_route.route('/cadastro')
def cadastro():
    item = Autor.novo()
    return render_template('./Autor/cadastro.html', item=item)


@autor_route.route('/cadastro/<int:id>')
def obter(id):
    item = Autor.obter(id)
    return render_template('./Autor/cadastro.html', item=item)


@autor_route.route('/cadastro', methods=['POST'])
def salvar():
    Autor.salvar(int(request.form['id']), request.form['nome'])
    return redirect('/autor')


@autor_route.route('/excluirAjax', methods=['POST'])
def excluirAjax():
    id = int(request.form.get('id', 0))
    if (id > 0):
        Autor.excluir(id)
    return jsonify({'status': 'success',
                    'message': 'Autor excluído com sucesso!'
                    }), 200


@autor_route.route('/cadastroAjax', methods=['POST'])
def cadastro_ajax():
    try:
        autor_salvo = Autor.salvar(int(request.form.get('id', 0)), request.form.get('nome'))
        
        lista_autores = Autor.listar()
        
        autores_json = [autor.to_dict() for autor in lista_autores]
        
        return jsonify({
            'status': 'success',
            'message': 'Autor salvo com sucesso!',
            'autores': autores_json 
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
