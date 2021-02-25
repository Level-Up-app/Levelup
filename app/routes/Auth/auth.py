from flask import Blueprint, jsonify, make_response, request, render_template
from flask_jwt_extended import create_access_token
from ...models import User
import datetime


auth_bp = Blueprint(
    'user', __name__, template_folder='templates', static_folder='static'
    )

@auth_bp.route('/auth/signup', methods=['POST'])
def sign_up():
    body = request.get_json()
    user = User(**body)
    user.hash_password()
    user.save()
    id = user.pk
    return jsonify({'result': 'user' + str(id)})

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    body = request.get_json()
    user = User.objects.get(email=body.get('email'))
    authorized = user.check_password(body.get('password'))
    if not authorized:
        jsonify({'result': 'nooooooo noooo!'})

    else: 
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.pk), expires_delta=expires)
        return jsonify({'result': access_token}), 200