from config.data_base import db

class Usuario(db.Model):
    __tablename__ = 'Usuario'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Integer, nullable=False)               # 1=Aluno,2=Professor,3=Visitante (exemplo)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Integer, nullable=False)             # 1=Ativo,2=Inativo,...
    observacao = db.Column(db.Text, nullable=True)

    
    @staticmethod
    def novo():
        return Usuario(
            id=0,
            tipo=1,
            nome="",
            cpf="",
            email="",
            telefone="",
            status=1,
            observacao=""
        )

    @staticmethod
    def obter(id):
        usuario = Usuario.query.get(id)
        if not usuario:
            raise UsuarioNaoEncontrado(f"Usuário com ID {id} não foi encontrado.")
        return usuario

    @staticmethod
    def listar():
        return Usuario.query.all()

    def salvar(self):
        if self.id and self.id > 0:
            db.session.merge(self)
        else:
            self.id = None
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def excluir(id):
        usuario = Usuario.query.get(id)
        if not usuario:
            raise UsuarioNaoEncontrado(f"Usuário com ID {id} não foi encontrado.")
        db.session.delete(usuario)
        db.session.commit()


class UsuarioNaoEncontrado(Exception):
    pass