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
   
    def to_dict(self):
        
        ds_condicoes = "Bom estado"
        if (self.condicoes == 2):
            ds_condicoes = "Médio estado"
        if (self.condicoes == 3):
            ds_condicoes = "Péssimo estado"
            
        return {"id": self.id, "localizacao": self.localizacao, "status": self.status, "ds_condicoes": ds_condicoes }  

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
    def listar(ids=None):
        query = Exemplar.query.options(
        db.joinedload(Exemplar.publicacao)
    )

        if ids:  # se veio lista de ids
            query = query.filter(Exemplar.id.in_(ids))

        return query.all()

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
