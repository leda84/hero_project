from flask import Blueprint, request, jsonify 
from hero_project.helpers import token_required
from hero_project.models import db, User, Character, character_schema, characters_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
@token_required 
def getdata(current_user_token):
    return {'some' : 'value',
            'other' : 'data'}

# Endpoint to create a character
@api.route('/characters', methods = ['POST'])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    alias = request.json['alias']
    description = request.json['description']
    comics_appeared_in = request.json['comics_appeared_in']
    super_power = request.json['super_power']
    user_token = current_user_token.token

    character = Character(name, alias, description, comics_appeared_in, super_power, user_token)
    db.session.add(character)
    db.session.commit()

    response = character_schema.dump(character)
    return jsonify(response)

# Endpoint to retrieve all characters
@api.route('/characters', methods = ['GET'])
@token_required
def get_characters(current_user_token):
    owner = current_user_token.token
    characters = Character.query.filter_by(user_token = owner).all()
    response = characters_schema.dump(characters)
    return jsonify(response)

# Endpoint to retrieve a single character
@api.route('/characters/<id>', methods = ['GET'])
@token_required
def get_car(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        character = Character.query.get(id)
        response = character_schema.dump(character)
        return jsonify(response)
    else:
        return jsonify({'message' : 'Valid Token Required'}), 401

# Endpoint to update a character
@api.route('/characters/<id>', methods = ['POST', 'PUT'])
@token_required
def update_character(current_user_token, id):
    character = Character.query.get(id)
    character.name = request.json['name']
    character.alias = request.json['alias']
    character.description = request.json['description']
    character.comics_appeared_in = request.json['comics_appeared_in']
    character.super_power = request.json['super_power']
    character.user_token = current_user_token.token

    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)

# Endpoint to delete a character
@api.route('/characters/<id>', methods = ['DELETE'])
@token_required
def delete_character(current_user_token, id):
    character = Character.query.get(id)
    print(character)
    db.session.delete(character)
    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)