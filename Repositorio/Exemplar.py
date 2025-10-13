from config.data_base import db
from Repositorio.Publicacao import Publicacao

class Exemplar(db.Model):
    __tablename__ = 'Exemplar'

    id = db.Column(db.Integer, primary_key=True)
    idPublicacao = db.Column(db.Integer, db.ForeignKey('Publicacao.id'), nullable=False)
    localizacao = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False)  
    condicoes = db.Column(db.Integer, nullable=False)

    publicacao = db.relationship('Publicacao', backref=db.backref('exemplares', lazy=True))

    @staticmethod
    def novo():
        return Exemplar(
            id=0,
            idPublicacao=0,
            localizacao="",
            status=1,
            condicoes=1
        )

    @staticmethod
    def obter(id):
        exemplar = Exemplar.query.get(id)
        if not exemplar:
            raise ExemplarNaoEncontrado(f"Exemplar com ID {id} não foi encontrado.")
        return exemplar

    @staticmethod
    def listar():
        return Exemplar.query.options(
            db.joinedload(Exemplar.publicacao)
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
        exemplar = Exemplar.query.get(id)
        if not exemplar:
            raise ExemplarNaoEncontrado(f"Exemplar com ID {id} não foi encontrado.")
        db.session.delete(exemplar)
        db.session.commit()


class ExemplarNaoEncontrado(Exception):
    pass
