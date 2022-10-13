# imported modules
from flask import Flask, jsonify, request, make_response
from flask_restframework import RestFramework, status
from email_validator import validate_email

def show_validation_error(message):
    return jsonify({'status': False, 'code': status.HTTP_400_BAD_REQUEST, 'message': message})
