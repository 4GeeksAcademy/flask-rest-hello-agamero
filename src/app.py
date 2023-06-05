"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import Character
from models import Homeworld
from models import Starships
from models import FavsCharacter
from models import FavsHomeworld
from models import FavsStarships


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Endpoint para obtener la información de un todos los character


@app.route('/character', methods=['GET'])
def get_all_characters():
    characters = Character.query.all()
    serialized_characters = [character.serialize() for character in characters]
    return jsonify(serialized_characters)

# Endpoint para obtener la información de un solo character


@app.route('/character/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        return jsonify({'mensaje': 'Personaje no encontrado'}), 404
    serialized_character = character.serialize()
    return jsonify(serialized_character)

# Endpoint para listar todos los registros de homeworld


@app.route('/homeworld', methods=['GET'])
def get_all_homeworlds():
    homeworlds = Homeworld.query.all()
    serialized_homeworlds = [homeworld.serialize() for homeworld in homeworlds]
    return jsonify(serialized_homeworlds)

# Endpoint para obtener la información de un solo homeworld


@app.route('/homeworld/<int:homeworld_id>', methods=['GET'])
def get_homeworld(homeworld_id):
    homeworld = Homeworld.query.get(homeworld_id)
    if homeworld is None:
        return jsonify({'mensaje': 'Planeta no encontrado'}), 404
    serialized_homeworld = homeworld.serialize()
    return jsonify(serialized_homeworld)

# Endpoint para listar todos los registros de starships


@app.route('/starships', methods=['GET'])
def get_all_starships():
    starships = Starships.query.all()
    serialized_starships = [starship.serialize() for starship in starships]
    return jsonify(serialized_starships)

# Endpoint para obtener la información de una sola starship


@app.route('/starships/<int:starship_id>', methods=['GET'])
def get_starship(starship_id):
    starship = Starships.query.get(starship_id)
    if starship is None:
        return jsonify({'mensaje': 'Nave no encontrada'}), 404
    serialized_starship = starship.serialize()
    return jsonify(serialized_starship)

# Endpoint para listar todos los usuarios del blog


@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    serialized_users = [user.serialize() for user in users]
    return jsonify(serialized_users)

# Endpoint para listar todos los favoritos de un usuario


@app.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_all__user_favorites(user_id):
    character_favorites = FavsCharacter.query.filter_by(user_id=user_id).all()
    homeworld_favorites = FavsHomeworld.query.filter_by(user_id=user_id).all()
    starship_favorites = FavsStarships.query.filter_by(user_id=user_id).all()

    serialized_favorites = {
        'characters': [fav.serialize() for fav in character_favorites],
        'homeworlds': [fav.serialize() for fav in homeworld_favorites],
        'starships': [fav.serialize() for fav in starship_favorites]
    }
    return jsonify(serialized_favorites)


@app.route('/users/<int:user_id>/homeworld/<int:homeworld_id>', methods=['POST'])
def add_favorite_homeworld(user_id, homeworld_id):
    # Verificar si el usuario existe en la base de datos
    user = User.query.get(user_id)
    if not user:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    # Verificar si el homeworld existe en la base de datos
    homeworld = Homeworld.query.get(homeworld_id)
    if not homeworld:
        return jsonify({'mensaje': 'Planeta no encontrado'}), 404

    # Crear un nuevo homeworld favorito para el usuario actual
    favorite_homeworld = FavsHomeworld(
        user_id=user_id, homeworld_id=homeworld_id)
    db.session.add(favorite_homeworld)
    db.session.commit()

    return jsonify({'mensaje': 'Planeta favorito agregado'}), 200


@app.route('/users/<int:user_id>/character/<int:character_id>', methods=['POST'])
def add_favorite_character(user_id, character_id):
    # Verificar si el usuario existe en la base de datos
    user = User.query.get(user_id)
    if not user:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    # Verificar si el character existe en la base de datos
    character = Character.query.get(character_id)
    if not character:
        return jsonify({'mensaje': 'Personaje no encontrado'}), 404

    # Crear un nuevo character favorito para el usuario actual
    favorite_character = FavsCharacter(
        user_id=user_id, character_id=character_id)
    db.session.add(favorite_character)
    db.session.commit()

    return jsonify({'mensaje': 'Personaje favorito agregado'}), 200


@app.route('/users/<int:user_id>/starships/<int:starships_id>', methods=['POST'])
def add_favorite_starships(user_id, starships_id):
    # Verificar si el usuario existe en la base de datos
    user = User.query.get(user_id)
    if not user:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    # Verificar si el starships existe en la base de datos
    starships = Starships.query.get(starships_id)
    if not starships:
        return jsonify({'mensaje': 'Nave no encontrada'}), 404

    # Crear un nuevo starships favorito para el usuario actual
    favorite_starships = FavsStarships(
        user_id=user_id, starships_id=starships_id)
    db.session.add(favorite_starships)
    db.session.commit()

    return jsonify({'mensaje': 'Nave favorita agregada'}), 200

@app.route('/favorite/homeworld/<int:homeworld_id>', methods=['DELETE'])
def delete_favorite_homeworld(homeworld_id):
    favorite_homeworld = FavsHomeworld.query.get(homeworld_id)
    if favorite_homeworld is None:
        return jsonify({'mensaje': 'Planeta favorito no encontrado'}), 404

    db.session.delete(favorite_homeworld)
    db.session.commit()

    return jsonify({'mensaje': 'Planeta favorito eliminado'}), 200


@app.route('/favorite/character/<int:character_id>', methods=['DELETE'])
def delete_favorite_character(character_id):
    favorite_character = FavsCharacter.query.get(character_id)
    if favorite_character is None:
        return jsonify({'mensaje': 'Personaje favorito no encontrado'}), 404

    db.session.delete(favorite_character)
    db.session.commit()

    return jsonify({'mensaje': 'Personaje favorito eliminado'}), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
