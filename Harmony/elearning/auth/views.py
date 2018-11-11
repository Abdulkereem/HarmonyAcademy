from flask import Blueprint , render_template,request,flash,jsonify,redirect,url_for
from models.users import *
import random
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from sqlalchemy.exc import *
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user 
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_mail import Mail, Message
from hashids import Hashids 
import random
from flask_uploads import UploadSet, configure_uploads, patch_request_class, DOCUMENTS




dig=random.randint(12222,408387388)
hashids = Hashids()

pbk = hashids.encode(dig)
pbk=str(pbk)
mail=Mail()
code = uuid.uuid4().hex
s = URLSafeTimedSerializer('5c3b1335d8924ea0822de9a8e657495f')


#configure_uploads(app, (cvs,), lambda app: '/static/uploads')

code=str(code)
login=Blueprint('login',__name__)

cvs = UploadSet('photos', DOCUMENTS)


@login.route('/siginup',methods=['POST'])
def signup():
	fname = request.form['fname']
	uname=request.form['username']
	email=request.form['email']
	password=request.form['password']
	hashed_password = generate_password_hash(password, method='sha256')
	new_user=Students(name=fname,
		username=uname,email=email,
                   password=hashed_password, private_key=code, is_student=True)
	try:
		db.session.add(new_user)
		db.session.commit()
		token = s.dumps(email, salt='email-confirm')
		msg = Message('Confirm Email', sender='Admin@guessrich.com', recipients=[email])
		link = url_for('login.confirm_email', token=token, _external=True)
		msg.body = str(code)+'Click This to Validate Your acount. {}'.format(link)
		mail.send(msg)
		flash('Account registration completed please check your email for verification')
		return redirect(url_for('main.index'))
	except IntegrityError:
		flash("Sorry user already exist")
		return redirect(url_for('main.index'))



@login.route('/register',methods=['POST'])
def register():
	fname = request.form['full_name']
	uname=request.form['uname']
	email=request.form['user_email']
	qualification=request.form['Your_Qalification']
	cv=request.files['cv']
	filename = cvs.save(cv)
	url = cvs.url(filename)
	password=request.form['user_password']
	hashed_password = generate_password_hash(password, method='sha256')
	new_user = Students(name=fname,
		username=uname,email=email,
		password=hashed_password,
                     resume=url, public_key=pbk, is_instructor=True)
	try:
		db.session.add(new_user)
		db.session.commit()
		token = s.dumps(email, salt='email-confirm')
		msg = Message('Confirm Email', sender='Admin@guessrich.com', recipients=[email])
		link = url_for('login.confirm_email', token=token, _external=True)
		msg.body = str(code)+'Click This to Validate Your acount. {}'.format(link)
		mail.send(msg)
		flash("registration successful")
		return redirect(url_for('dash.dashboard'))
	except IntegrityError:
		flash("Sorry user already exist")
		return redirect(url_for('main.index'))








@login.route('/signin',methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	user=Students.query.filter_by(username=username).first()
	if user:
		if check_password_hash(user.password,password):
			login_user(user)
			return redirect(url_for('dash.dashboard'))
	else:
		flash("invalid username or password")
		return redirect(url_for('main.index'))

@login.route('/confirm_email/<token>')
def confirm_email(token):
	try:
		email = s.loads(token, salt='email-confirm', max_age=3600)
		return("valid")
	except SignatureExpired:
		return '<h1>The token as expired!</h1>'















@login.route('/logout')
def logout():
	logout_user()
	flash("sign out successful")
	return redirect(url_for('main.index'))




