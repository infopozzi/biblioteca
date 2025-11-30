from flask import Blueprint, render_template, request, redirect, jsonify
from Repositorio.Emprestimo import Emprestimo
from Repositorio.Usuario import Usuario, UsuarioNaoEncontrado
from Repositorio.Publicacao import Publicacao
from Repositorio.Exemplar import Exemplar

emprestimo_route = Blueprint('emprestimo', __name__)


@emprestimo_route.route('/')
def listar():
    idUsuario = request.args.get('idUsuario', type=int)
    situacao = request.args.get('status')

    lista = Emprestimo.listar(idUsuario = idUsuario, situacao= situacao )
    return render_template('./emprestimo/index.html', lista=lista, listaCliente = Usuario.listar())


@emprestimo_route.route('/cadastro')
def cadastro():
    item = Emprestimo.novo()
    listaPublicacoes = Publicacao.listar()
    return render_template('./emprestimo/cadastro.html', item=item, listaCliente = Usuario.listar(), listaPublicacoes = listaPublicacoes)


@emprestimo_route.route('/cadastro/<int:id>')
def obter(id):
    item = Emprestimo.obter(id)

    lista_ids = [int(x) for x in item.lsLivros.split(",") if x]

    lsEmprestimo = Exemplar.listar(lista_ids)
    
    return render_template('./emprestimo/cadastro.html', item=item, listaCliente = Usuario.listar(), lsEmprestimo = lsEmprestimo)


@emprestimo_route.route('/cadastro', methods=['POST'])
def salvar():
    Emprestimo.salvar(int(request.form['id']), 1, request.form['idCliente'], request.form['dtCadastro'], request.form['dtPrevisaoEntrega'], request.form['dtEntregaEfetiva'], request.form['lsLivros'])
    
    lista_ids = [int(x) for x in request.form['lsLivros'].split(",") if x]
    for item in Exemplar.listar(lista_ids):
        item.status = request.form['dtEntregaEfetiva'] != ''
        Exemplar.salvar(item)      
        
    return redirect('/emprestimo')


@emprestimo_route.route('/excluirAjax', methods=['POST'])
def excluirAjax():
    id = int(request.form.get('id', 0))
    if (id > 0):
        Emprestimo.excluir(id)
    return jsonify({'status': 'success',
                    'message': 'Autor excluído com sucesso!'
                    }), 200


@emprestimo_route.route('/exemplaresAjax', methods=['POST'])
def exemplares_ajax():
    try:
        publicacao = Publicacao.obter(int(request.form.get('id', 0)))

        exemplares_json = [e.to_dict() for e in publicacao.exemplares if e.status == 1]

        return jsonify({
            'status': 'success',
            'message': 'lista de exemplares',
            'exemplares': exemplares_json 
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


