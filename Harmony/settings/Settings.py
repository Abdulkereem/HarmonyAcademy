from models.users import *
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user 


def Setting_Page():
	config=settings.query.first()
	if config.maitinance_mode==True:
		msg="<h1>Sorry under maintainance mode!!!</h1>"
		return msg
	else:
		return('test')
		