from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    raca = db.Column(db.String(50))
    data_resgate = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return f'<Animal {self.nome}>'

class Doacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.Date, nullable=False)
    doador_id = db.Column(db.Integer, db.ForeignKey('doador.id'), nullable=False)
    
    def __repr__(self):
        return f'<Doacao {self.id}>'

class Doador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Doador {self.nome}>'