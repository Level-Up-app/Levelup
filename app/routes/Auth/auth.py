from flask import Blueprint, jsonify, Response, request, render_template, redirect, url_for
from flask_jwt_extended import create_access_token
from mongoengine.errors import NotUniqueError, FieldDoesNotExist
from ...models import User
import datetime


auth_bp = Blueprint(
    'user', __name__, template_folder='templates', static_folder='static'
    )

@auth_bp.route('/auth', methods=['GET'])
def show_signup_login_page():
    return render_template('auth.html')


@auth_bp.route('/auth', methods=['POST'])
def signup():
    if request.form['signup-name'] or request.form['signup-email'] or request.form['signup-password']:
        print(request.form)
        try:
            user = User(
                    name=request.form.get('signup-name'), 
                    email=request.form.get('signup-email'), 
                    password=request.form.get('signup-password')
                    )
            user.hash_password()
            user.save()

            return render_template('habits.html', user=user.name)
        # except FieldDoesNotExist:
        #     return render_template('auth.html', error_message='Missing required fields')
        except NotUniqueError as es:
            return redirect('auth' )

    else:
        try:
            user = User.objects.get(email=request.form.get('login-email'))
            authorized = user.check_password(request.form.get('login-password'))
            
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.pk), expires_delta=expires)
            return render_template('habits.html', user=user.name), 200

        except Exception as e:
            return jsonify({'result': str(e)})