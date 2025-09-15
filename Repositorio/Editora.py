from config.data_base import db 

class Editora(db.Model):
    __tablename__ = 'Editora'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

    def to_dict(self):
        return {"id": self.id, "nome": self.nome }  

    @staticmethod
    def novo():
        editora = Editora(id = 0, nome = "")
        return editora

    @staticmethod
    def obter(id):
        editora = Editora.query.get(id)
        if not editora:
            raise EditoraNaoEncontrado(f"Editora com ID {id} não foi encontrado.")
        return editora

    @staticmethod
    def listar():
        editora = Editora.query.all()
        return editora
    
    @staticmethod
    def salvar(id, nome):
        if id > 0:            
            editora = Editora.query.get(id)
            editora.nome = nome
        else: 
            editora = Editora(nome = nome)        
            db.session.add(editora)

        db.session.commit()
        return editora
    
    @staticmethod
    def excluir(id):
        editora = Editora.query.get(id)
        if not editora:
            raise EditoraNaoEncontrado(f"Editora com ID {id} não foi encontrado.")
        db.session.delete(editora)
        db.session.commit()


class EditoraNaoEncontrado(Exception):
    pass
