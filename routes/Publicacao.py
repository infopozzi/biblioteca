from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from Repositorio.Publicacao import Publicacao
from Repositorio.Autor import Autor
from Repositorio.Categoria import Categoria
from Repositorio.Editora import Editora


publicacao_route = Blueprint('publicacao', __name__)

# --- Rota para a página de listagem ---
@publicacao_route.route('/')
def index():
    lista_publicacoes = Publicacao.listar()
    return render_template('publicacao/index.html', lista=lista_publicacoes)

# --- Rota para o formulário de cadastro (GET) e para salvar (POST) ---
@publicacao_route.route('/cadastro', methods=['GET', 'POST'])
@publicacao_route.route('/cadastro/<int:id>', methods=['GET', 'POST'])
def cadastro(id=0):
    if request.method == 'POST':
        # Pega o ID do formulário (0 se for um novo cadastro)
        id_formulario = request.form.get('id', 0, type=int)
        
        # Busca a publicação no banco se for uma edição, ou cria uma nova se for cadastro
        item = Publicacao.obter(id_formulario) if id_formulario > 0 else Publicacao()

        # Pega os dados 
        id_autor = request.form.get('idAutor')
        id_categoria = request.form.get('idCategoria')
        id_editora = request.form.get('idEditora')
        
        # Validação dos campos obrigatórios
        if not id_autor or not id_categoria or not id_editora:
            return "Erro: Autor, Categoria e Editora são campos obrigatórios.", 400

        # Preenche o objeto 'item'
        item.idAutor = int(id_autor)
        item.idCategoria = int(id_categoria)
        item.idEditora = int(id_editora)
        item.idTipo = request.form.get('idTipo', type=int)
        item.ano = request.form.get('ano', type=int)
        item.titulo = request.form.get('titulo')
        item.descricao = request.form.get('descricao')
        #item.qtdeTotal = request.form.get('qtdeTotal', type=int)
        #item.qtdeDisponivel = request.form.get('qtdeDisponivel', type=int)

        # Salva o item no banco de dados
        item.salvar()
        
        # Redireciona o usuário para a página de listagem
        return redirect(url_for('publicacao.index'))
    
    item = Publicacao.novo() if id == 0 else Publicacao.obter(id)
    
    # Busca as listas
    lista_autores = Autor.listar()
    lista_categorias = Categoria.listar()
    lista_editoras = Editora.listar()

    return render_template(
        'publicacao/cadastro.html', 
        item=item,
        listaAutores=lista_autores,
        listaCategoria=lista_categorias,
        listaEditora=lista_editoras
    )

# --- Rota para a exclusão via JavaScript (AJAX) ---
@publicacao_route.route('/excluirAjax', methods=['POST'])
def excluir_ajax():
    try:
        id_pub = request.form.get('id')
        Publicacao.excluir(id_pub)
        return jsonify({'status': 'OK', 'message': 'Publicação excluída com sucesso.'})
    except Exception as e:
        return jsonify({'status': 'ERROR', 'message': str(e)}), 400