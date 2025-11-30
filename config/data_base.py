from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """
    Inicializa a base de dados com o app Flask e o SQLAlchemy.
    """
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:ga0800@localhost/bibliotecaV2" #Gabriel
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://sa:gin_adm1@localhost/bibliotecav2"  #Alexandre
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:msm152931@localhost/bibliotecaV2"   #Matheus
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://viniCODEX:bE1rp021@localhost/editora_db" #Vinicius
    
    #app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:ga0800@localhost/bibliotecaV2"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
