import os
from flask_admin import Admin
from models import db, User
from models import db, Character
from models import db, Starships
from models import db, Homeworld
from models import db, FavsCharacter
from models import db, FavsHomeworld
from models import db, FavsStarships


from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class CharacterAdmin(ModelView):
        column_list = ("id", "name", "birth_year", "eye_color", "gender", "hair_color", "height", "films", "homeworld_id", "mass", "skin_color", "species", "starships_id", "url", "vehicles")
        form_columns = ("name", "birth_year", "eye_color", "gender", "hair_color", "height", "films", "homeworld_id", "mass", "skin_color", "species", "starships_id", "url", "vehicles")
        column_hide_backrefs = False
    
    class FavsCharacterAdmin(ModelView):
        column_list = ("id", "user_id", "character_id")
        form_columns = ("user_id", "character_id")
        column_hide_backrefs = False

    class FavsStarshipsAdmin(ModelView):
        column_list = ("id", "user_id", "starships_id")
        form_columns = ("user_id", "starships_id")
        column_hide_backrefs = False
    
    class FavsHomeworldAdmin(ModelView):
        column_list = ("id", "user_id", "homeworld_id")
        form_columns = ("user_id", "homeworld_id")
        column_hide_backrefs = False
    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(CharacterAdmin(Character, db.session))
    admin.add_view(ModelView(Starships, db.session))
    admin.add_view(ModelView(Homeworld, db.session))
    admin.add_view(FavsCharacterAdmin(FavsCharacter, db.session))
    admin.add_view(FavsHomeworldAdmin(FavsHomeworld, db.session))
    admin.add_view(FavsStarshipsAdmin(FavsStarships, db.session))




    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))