from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from models.users import *
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('./home/index.html')

@main.route('/create')
def create():
    db.create_all()
    return ("DONE")

@main.route('/drop')
def delete():
    db.drop_all()
    return("drop")