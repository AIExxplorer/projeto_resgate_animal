from flask import render_template, jsonify
from app import app, db
from app.models import Animal, Doacao, Doador

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/animais')
def get_animais():
    animais = Animal.query.all()
    return jsonify([{'id': a.id, 'nome': a.nome, 'especie': a.especie} for a in animais])

@app.route('/api/doacoes')
def get_doacoes():
    doacoes = Doacao.query.all()
    return jsonify([{'id': d.id, 'valor': d.valor, 'data': d.data.isoformat()} for d in doacoes])

@app.route('/api/doadores')
def get_doadores():
    doadores = Doador.query.all()
    return jsonify([{'id': d.id, 'nome': d.nome, 'email': d.email} for d in doadores])