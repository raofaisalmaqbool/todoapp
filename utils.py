# imported modules
from flask import Flask, jsonify, request, make_response
from flask_restframework import RestFramework, status
from email_validator import validate_email

def show_validation_error(message):
    """This will show validation message or status responce may be change of validation function"""
    return jsonify({'status': False, 'code': status.HTTP_400_BAD_REQUEST, 'message': message})


def exception_error(message):
    """this will show exception message or status responce may be change of exception hendeler function"""
    return jsonify({'status': False, 'code': status.HTTP_400_BAD_REQUEST, 'message': message})


def created_message(message):
    """it will show success message status and responce may be change of this function"""
    return jsonify({'status':True, 'code':status.HTTP_201_CREATED, 'message': message})