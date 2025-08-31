from flask import Flask
from config.data_base import init_db

from routes.Login import login_route
from routes.Index import index_route
from routes.Autor import autor_route
#from routes.Categoria import categoria_route
#from routes.Editora import editora_route
#from routes.Publicacao import publicacao_route
#rom routes.Exemplar import exemplar_route
#from routes.Relatorio import relatorio_route
#from routes.Usuario import usuario_route

app = Flask(__name__)
app.secret_key = 'codigoSecreto'

init_db(app)

app.register_blueprint(index_route)
app.register_blueprint(login_route, url_prefix='/login')
app.register_blueprint(autor_route, url_prefix='/autor')
#app.register_blueprint(categoria_route, url_prefix='/categoria')
#app.register_blueprint(editora_route, url_prefix='/editora')
#app.register_blueprint(publicacao_route, url_prefix='/publicacao')
#app.register_blueprint(exemplar_route, url_prefix='/exemplar')
#app.register_blueprint(relatorio_route, url_prefix='/relatorio')
#app.register_blueprint(usuario_route, url_prefix='/usuario')


app.run(debug=True)