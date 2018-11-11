from flask import Flask
from flask_admin import Admin
from flask_mail import Mail, Message
from flask_admin.contrib.sqla import ModelView
from models.users import *
from home.view import main
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from flask_uploads import UploadSet, configure_uploads, patch_request_class, DOCUMENTS

import os



app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config['EXPLAIN_TEMPLATE_LOADING']=True
app.config['TEMPLATES_AUTO_RELOAD']=True

app.config['ALLOWED_EXTENSIONS'] = set([DOCUMENTS])
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+'/static/uploads'

cvs = UploadSet('photos', DOCUMENTS)
configure_uploads(app, (cvs))
#configure_uploads(app, (cvs), lambda app: '/static/uploads')

patch_request_class(app)

mail =Mail(app)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'
from home.view import main
from auth.views import login
from dashboard.view import dash

@login_manager.user_loader
def load_user(user_id):
    return Students.query.get(int(user_id))


admin = Admin(app, name='Control Panel')
admin.add_view(ModelView(Students, db.session))
#admin.add_view(ModelView(Teachers, db.session))
admin.add_view(ModelView(Books,db.session))
admin.add_view(ModelView(Courses, db.session))
admin.add_view(ModelView(Lectures,db.session))
admin.add_view(ModelView(settings,db.session))

app.register_blueprint(home.view.main)
app.register_blueprint(auth.views.login)
app.register_blueprint(dashboard.view.dash)
