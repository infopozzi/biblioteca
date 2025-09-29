from config.data_base import db
from Repositorio.Autor import Autor
from Repositorio.Categoria import Categoria
from Repositorio.Editora import Editora


class Publicacao(db.Model):
    __tablename__ = 'Publicacao'
    id = db.Column(db.Integer, primary_key=True)

    idAutor = db.Column(db.Integer, db.ForeignKey('Autor.id'), nullable=False)
    idCategoria = db.Column(db.Integer, db.ForeignKey(
        'Categoria.id'), nullable=False)
    idEditora = db.Column(db.Integer, db.ForeignKey(
        'Editora.id'), nullable=False)

    idTipo = db.Column(db.Integer, nullable=False)  
    ano = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    qtdeTotal = db.Column(db.Integer, default=0, nullable=False)
    qtdeDisponivel = db.Column(db.Integer, default=0, nullable=False)

    autor = db.relationship(
        'Autor', backref=db.backref('publicacoes', lazy=True))
    categoria = db.relationship(
        'Categoria', backref=db.backref('publicacoes', lazy=True))
    editora = db.relationship(
        'Editora', backref=db.backref('publicacoes', lazy=True))

    @staticmethod
    def novo():
        return Publicacao(
            id=0, idAutor=0, idCategoria=0, idEditora=0, idTipo=0,
            ano="", titulo="", descricao="", qtdeTotal=1, qtdeDisponivel=1
        )

    @staticmethod
    def obter(id):
        publicacao = Publicacao.query.get(id)
        if not publicacao:
            raise PublicacaoNaoEncontrada(
                f"Publicação com ID {id} não foi encontrada.")
        return publicacao

    @staticmethod
    def listar():
        return Publicacao.query.options(
            db.joinedload(Publicacao.autor),
            db.joinedload(Publicacao.categoria),
            db.joinedload(Publicacao.editora)
        ).all()

    def salvar(self):
        if self.id and self.id > 0:
            db.session.merge(self)
        else:
            self.id = None  
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def excluir(id):
        publicacao = Publicacao.query.get(id)
        if not publicacao:
            raise PublicacaoNaoEncontrada(
                f"Publicação com ID {id} não foi encontrada.")
        db.session.delete(publicacao)
        db.session.commit()



class PublicacaoNaoEncontrada(Exception):
    pass
