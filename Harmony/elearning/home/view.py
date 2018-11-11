from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from models.users import *
from settings.Settings import Setting_Page
main = Blueprint('main', __name__)

@main.route('/')
def index():
	config=settings.query.first()
	if config.maitinance_mode==True:
		msg="<h1>Sorry under maintainance mode!!!</h1>"
		return msg
	else:
		pass
	return render_template('./home/index.html')

@main.route('/create')
def create():
	config=settings.query.first()
	if config.maitinance_mode==True:
		msg="<h1>Sorry under maintainance mode!!!</h1>"
		return msg
	else:
		pass
	db.create_all()
	return ("DONE")

@main.route('/drop')
def delete():
	config=settings.query.first()
	if config.maitinance_mode==True:
		msg="<h1>Sorry under maintainance mode!!!</h1>"
		return msg
	else:
		pass
	#Setting_Page()
	db.drop_all()
	return("drop")