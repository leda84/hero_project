from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('get/data')
def getdata():
    return {'some' : 'value',
            'other' : 'data'}
