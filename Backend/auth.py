from flask import jsonify, request
from constants import HTTP

def login_with_email(firebase):
    # TEST
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify(error=HTTP.UNAUTHORIZED.value)
    
    return firebase.auth().sign_in_with_email_and_password(email, password)