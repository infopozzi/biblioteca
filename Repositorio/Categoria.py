from config.data_base import db 

class Categoria(db.Model):
    __tablename__ = 'Categoria'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

    def to_dict(self):
        return {"id": self.id, "nome": self.nome }  

    @staticmethod
    def novo():
        categoria = Categoria(id = 0, nome = "")
        return categoria

    @staticmethod
    def obter(id):
        categoria = Categoria.query.get(id)
        if not categoria:
            raise CategoriaNaoEncontrado(f"Categoria com ID {id} não foi encontrado.")
        return categoria

    @staticmethod
    def listar():
        categoria = Categoria.query.all()
        return categoria
    
    @staticmethod
    def salvar(id, nome):
        if id > 0:            
            categoria = Categoria.query.get(id)
            categoria.nome = nome
        else: 
            categoria = Categoria(nome = nome)        
            db.session.add(categoria)

        db.session.commit()
        return categoria
    
    @staticmethod
    def excluir(id):
        categoria = Categoria.query.get(id)
        if not categoria:
            raise CategoriaNaoEncontrado(f"Categoria com ID {id} não foi encontrado.")
        db.session.delete(categoria)
        db.session.commit()


class CategoriaNaoEncontrado(Exception):
    pass
