from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .models import db, Animal

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/add_animal', methods=['GET', 'POST'])
def add_animal():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        breed = request.form.get('breed')
        age = request.form.get('age')
        sex = request.form['sex']
        rescue_date = request.form['rescue_date']
        medical_history = request.form.get('medical_history')

        new_animal = Animal(
            name=name,
            species=species,
            breed=breed,
            age=age,
            sex=sex,
            rescue_date=rescue_date,
            medical_history=medical_history
        )
        db.session.add(new_animal)
        db.session.commit()
        return redirect(url_for('main.list_animals'))
    return render_template('add_animal.html')

@main_blueprint.route('/list_animals')
def list_animals():
    animals = Animal.query.all()
    return render_template('list_animals.html', animals=animals)