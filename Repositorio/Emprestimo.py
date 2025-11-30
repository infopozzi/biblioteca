from config.data_base import db 
from datetime import datetime

class Emprestimo(db.Model):
    __tablename__ = 'Emprestimo'
    id = db.Column(db.Integer, primary_key=True)
    idFuncionario = db.Column(db.Integer, nullable=False)
    idCliente = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=False)
    dtCadastro = db.Column(db.String(100), nullable = False)
    dtPrevisaoEntrega = db.Column(db.String(100), nullable = False)
    dtEntregaEfetiva = db.Column(db.String(100), nullable = False)
    status = db.Column(db.Integer, nullable=False)  
    lsLivros = db.Column(db.String(100), nullable = False)

    def to_dict(self):
        return {"id": self.id, "livros": self.lsLivros }  

    usuario = db.relationship(
        'Usuario', backref=db.backref('emprestimo', lazy=True))
    
    @property
    def situacao(self):
        hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        if (not self.dtPrevisaoEntrega):
            return "Desconhecido"

        # Converte as datas (se estiverem em string)
        dtPrev = datetime.fromisoformat(self.dtPrevisaoEntrega)
        dtEnt = None
        if self.dtEntregaEfetiva and self.dtEntregaEfetiva != "":  
            dtEnt = datetime.fromisoformat(self.dtEntregaEfetiva)

        # Regras:
        if dtEnt is not None:
            return "Concluído"
        if dtPrev < hoje:
            return "Atrasado"
        if dtPrev >= hoje:
            return "Emprestado"

        return "Desconhecido"

    @staticmethod
    def novo():
        emprestimo = Emprestimo(id = 0, dtPrevisaoEntrega = "", dtEntregaEfetiva = "", lsLivros = "")
        return emprestimo

    @staticmethod
    def obter(id):
        emprestimo = Emprestimo.query.get(id)
        if not emprestimo:
            raise AutorNaoEncontrado(f"Autor com ID {id} não foi encontrado.")
        return emprestimo

    @staticmethod
    def listar(idUsuario=None, situacao=None):
        query = Emprestimo.query

        if idUsuario:
            query = query.filter(Emprestimo.idCliente == idUsuario)

        emprestimos = query.all()

        if situacao:
            emprestimos = [e for e in emprestimos if e.situacao == situacao]

        return emprestimos

    @staticmethod
    def salvar(id, idFuncionario, idCliente, dtCadastro, dtPrevisaoEntrega, dtEntregaEfetiva, lsLivros):
        if id > 0:            
            emprestimo = Emprestimo.query.get(id)
            emprestimo.idFuncionario = idFuncionario
            emprestimo.idCliente = idCliente
            emprestimo.dtCadastro = dtCadastro
            emprestimo.dtPrevisaoEntrega = dtPrevisaoEntrega
            emprestimo.dtEntregaEfetiva = dtEntregaEfetiva
            emprestimo.lsLivros = lsLivros

        else: 
            emprestimo = Emprestimo(idFuncionario = idFuncionario,
                                    idCliente = idCliente,
                                    dtCadastro = dtCadastro,
                                    dtPrevisaoEntrega = dtPrevisaoEntrega,
                                    dtEntregaEfetiva = dtEntregaEfetiva,
                                    status = 0, 
                                    lsLivros = lsLivros)        
            db.session.add(emprestimo)

        db.session.commit()
        return emprestimo
    
    @staticmethod
    def excluir(id):
        emprestimo = Emprestimo.query.get(id)
        if not emprestimo:
            raise AutorNaoEncontrado(f"Autor com ID {id} não foi encontrado.")
        db.session.delete(emprestimo)
        db.session.commit()


class AutorNaoEncontrado(Exception):
    pass
