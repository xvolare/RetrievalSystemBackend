from flask import Blueprint, request
from services.user import user_login
user = Blueprint('user', __name__)

@user.route('login', methods=['POST'])
def login():
    data = request.form
    email = data['email']
    password = data['password']
    # ?
    data = user_login(email, password)
    return data