from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """
    Inicializa a base de dados com o app Flask e o SQLAlchemy.
    """
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@mysql57:3306/market_management'
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://sa:gin_adm1@localhost/bibliotecav2"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()