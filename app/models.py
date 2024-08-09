from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    raca = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(10))
    data_resgate = db.Column(db.Date, nullable=False)
    historico_medico = db.Column(db.Text)

class Adotante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    contato = db.Column(db.String(100))
    data_adocao = db.Column(db.Date, nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)

class Doador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    contato = db.Column(db.String(100))
    email = db.Column(db.String(100),  unique=True, nullable=False)  # Adicionando o atributo email
    historico_doacoes = db.Column(db.Text)

class Voluntario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    contato = db.Column(db.String(100))
    funcao = db.Column(db.String(100))
    disponibilidade = db.Column(db.String(100))

class Doacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    doador_id = db.Column(db.Integer, db.ForeignKey('doador.id'), nullable=False)