from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash
# ^^^ to add security hashing to passwords so they can't be seen

import secrets
# ^^^import for Secrets Module(given by Python)
from flask_login import LoginManager, UserMixin, login_manager
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# this will make a "user" table in database along with its components/columns
class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default='')
    last_name = db.Column(db.String(150), nullable = True, default='')
    email = db.Column(db.String(150), nullable = False) #false cause everyone should imput an email
    password = db.Column(db.String, nullable = True, default='') #true cause if you're linking an account, no password is needed
    g_auth_verify = db.Column(db.Boolean, default=False)
    token = db.Column(db.String, default='', unique=True) #unique so no one can have the same token
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    character = db.relationship('Character', backref = "owner", lazy = True)

    def __init__(self, email, first_name = '', last_name = '', id = '', password = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def set_token(self, length):
        return secrets.token_hex(length)

    def __repr__(self):
        return f'User {self.email} has been added to the Database.'

    class Character(db.Model):
        id = db.Column(db.String, primary_key = True)
        name = db.Column(db.String(150))
        alias = db.Column(db.String(150), nullable = True)
        description = db.Column(db.String(200), nullable = True)
        comics_appeared_in = db.Column(db.Integer)
        super_power = db.Column(db.String(150), nullable = False)
        date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
        user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)


        def __init__(self, name, alias, description, comics_appeared_in, super_power, user_token, id = ""):
            self.id = self.set_id()
            self.name = name
            self.alias = alias
            self.description = description
            self.comics_appeared_in = comics_appeared_in
            self.super_power = super_power
            self.user_token = user_token

        def set_id(self):
            return secrets.token_urlsafe()

        def __repr__(self):
            return f'The following superhero has been created: {self.name}'
