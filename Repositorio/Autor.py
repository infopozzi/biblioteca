from config.data_base import db 

class Autor(db.Model):
    __tablename__ = 'Autor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

    def to_dict(self):
        return {"id": self.id, "nome": self.nome }  

    @staticmethod
    def novo():
        autor = Autor(id = 0, nome = "")
        return autor

    @staticmethod
    def obter(id):
        autor = Autor.query.get(id)
        if not autor:
            raise AutorNaoEncontrado(f"Autor com ID {id} não foi encontrado.")
        return autor

    @staticmethod
    def listar():
        autor = Autor.query.all()
        return autor
    
    @staticmethod
    def salvar(id, nome):
        if id > 0:            
            autor = Autor.query.get(id)
            autor.nome = nome
        else: 
            autor = Autor(nome = nome)        
            db.session.add(autor)

        db.session.commit()
        return autor
    
    @staticmethod
    def excluir(id):
        autor = Autor.query.get(id)
        if not autor:
            raise AutorNaoEncontrado(f"Autor com ID {id} não foi encontrado.")
        db.session.delete(autor)
        db.session.commit()


class AutorNaoEncontrado(Exception):
    pass
