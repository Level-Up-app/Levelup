from flask import Blueprint, jsonify, make_response, request, render_template
from flask_jwt_extended import create_access_token
from mongoengine.errors import NotUniqueError
from ...models import User
import datetime


auth_bp = Blueprint(
    'user', __name__, template_folder='templates', static_folder='static'
    )

@auth_bp.route('/auth', methods=['GET'])
def show_signup_login_page():
    return render_template('auth.html')


@auth_bp.route('/auth', methods=['POST'])
def login_signup():
    is_signup = True
    print(request.form)
    for key in request.form:
        if key == "signup":
            print("****************")
        # user = handle_signup()
            return render_template('home.html')
        else:
            print("failed")
    # else:
    #     body = request.get_json()
    #     user = User.objects.get(email=body.get('email'))
    #     authorized = user.check_password(body.get('password'))
    #     if not authorized:
    #         jsonify({'result': 'nooooooo noooo!'})

    #     else: 
    #         expires = datetime.timedelta(days=7)
    #         access_token = create_access_token(identity=str(user.pk), expires_delta=expires)
    #         return jsonify({'result': access_token}), 200
    # return jsonify({'results': 'something went wrong'})




def handle_signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = User(name, email, password)
        user.hash_password()
        user.save()
        return user.name
    except NotUniqueError:
        print('something went wrong')
    