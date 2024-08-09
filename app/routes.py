from flask import Blueprint, request, jsonify, render_template
from .models import db, Animal, Adotante, Doador, Voluntario, Doacao

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/animals', methods=['POST'])
def add_animal():
    data = request.get_json()
    new_animal = Animal(
        name=data['name'],
        species=data['species'],
        breed=data.get('breed'),
        age=data.get('age'),
        sex=data['sex'],
        rescue_date=data['rescue_date'],
        medical_history=data.get('medical_history')
    )
    db.session.add(new_animal)
    db.session.commit()
    return jsonify({"message": "Animal adicionado com sucesso!"}), 201

@main_blueprint.route('/animals', methods=['GET'])
def get_animals():
    animals = Animal.query.all()
    return jsonify([{
        "id": animal.id,
        "name": animal.name,
        "species": animal.species,
        "breed": animal.breed,
        "age": animal.age,
        "sex": animal.sex,
        "rescue_date": str(animal.rescue_date),
        "medical_history": animal.medical_history
    } for animal in animals])