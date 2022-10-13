# imported modules

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, make_response
from flask_restframework import RestFramework, status
from email_validator import validate_email
from utils import *


# app settings
app = Flask(__name__)
app.config['SECRET_KEY'] = '\xdelg\x1c\xf6\xcaP\x1a?\x0b\xb3|\xa0c\xb0\x8c\xe8\xfc\xea\xb6\x10\xfe\xf0I'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todoapp.db"
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
db = SQLAlchemy(app)


# Table of User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    tasks = db.relationship('Task', backref='creator', lazy=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


    def __repr__(self):
        return f"User('{self.username}')"


# Table of Task that can add a user
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f"User('{self.title}')"


@app.route('/sign_up', methods=['POST'])
def sign_up():

    """sign up for the user should be valid username password and unique email"""
    try:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user_exist = User.query.filter_by(email=email).first()
        if user_exist:
            return jsonify({'status': False, 'code': status.HTTP_400_BAD_REQUEST,
                            'message': "User already exit with this email. Please enter a unique email."})
        else:
            email = validate_email(email)
            if len(password) <= 6:
                message = "Password Should be greater or equel to 6 digits......."
                return show_validation_error(message)

            user = User(username=username, password=password, email=email) # passwork should be encrypeted
            db.session.add(user)
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'status':False, 'code':status.HTTP_400_BAD_REQUEST, 'message': str(e)})
    return jsonify({'status':True, 'code':status.HTTP_201_CREATED, 'message': "User created successfully."})

if __name__ == '__main__':
    app.run()
