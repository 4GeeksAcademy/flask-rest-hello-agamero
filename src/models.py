from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favs_characters = db.relationship('FavsCharacter', backref='user', lazy=True)
    favs_starships = db.relationship('FavsStarships', backref='user', lazy=True)
    favs_homeworld = db.relationship('FavsHomeworld', backref='user', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    homeworld_id = db.Column(db.Integer, ForeignKey('homeworld.id'))
    mass = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    species = db.Column(db.String(250), nullable=False)
    starships_id = db.Column(db.Integer, ForeignKey('starships.id'))
    url = db.Column(db.String(250), nullable=False)
    vehicles = db.Column(db.String(250), nullable=False)
    favs_Character = db.relationship('FavsCharacter', backref='character', lazy=True)


    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "films": self.films,
            "homeworld_id": self.homeworld_id,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "species": self.species,
            "starships_id": self.starships_id,
            "url": self.url,
            "vehicles": self.vehicles,

            # do not serialize the password, its a security breach
        }

class Starships(db.Model):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    MGLT = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250))
    consumables = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    hyperdrive_rating = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    pilots = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    favs_Starships = db.relationship('FavsStarships', backref='starships', lazy=True)


    def __repr__(self):
        return '<Starships %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "hyperdrive_rating": self.hyperdrive_rating,
            "lengt": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "passengers": self.passengers,
            "films": self.films,
            "pilots": self.pilots,
            "starship_class": self.starship_class,
            "url": self.url,
            # do not serialize the password, its a security breach
        }

class Homeworld(db.Model):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    residents = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    favs_Homeworld = db.relationship('FavsHomeworld', backref='homeworld', lazy=True)


    def __repr__(self):
        return '<Homeworld %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "films": self.films,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "residents": self.residents,
            "residents": self.residents,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "url": self.url,
            # do not serialize the password, its a security breach
        }

class FavsCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, ForeignKey('character.id'))

    def __repr__(self):
        return '<FavsCharacter %r>' % self.id

    def serialize(self):
        query_character = Character.query.filter_by(id = self.character_id).first()
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_info": query_character.serialize(),
            # do not serialize the password, its a security breach
        }

class FavsStarships(db.Model):
    __tablename__ = 'StarshipsFavs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'))

    def __repr__(self):
        return '<FavsStarships %r>' % self.id

    def serialize(self):
        query_starships = Starships.query.filter_by(id=self.starships_id).first()
        return {
            "id": self.id,
            "user_id": self.user_id,
            "starships_id": query_starships.serialize(),
            # do not serialize the password, it's a security breach
        }

class FavsHomeworld(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    homeworld_id = db.Column(db.Integer, ForeignKey('homeworld.id'))

    def __repr__(self):
        return '<FavsHomeworld %r>' % self.id

    def serialize(self):
        query_homeworld = Homeworld.query.filter_by(id=self.homeworld_id).first()
        return {
            "id": self.id,
            "user_id": self.user_id,
            "homeworld_id": query_homeworld.serialize(),
            # do not serialize the password, it's a security breach
        }
