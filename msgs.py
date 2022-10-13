# imported modules
from flask import Flask, jsonify, request, make_response
from flask_restframework import RestFramework, status
from email_validator import validate_email
from utils import *

def passwork_error_msg():
    return "Password Should be greater or equel to 6 digits."

def user_already_exist():
    return "User already exit with this email. Please enter a unique email."