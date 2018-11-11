from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import random


first_key=uuid.uuid4()
first_key=str(first_key)
hashed_key = generate_password_hash(first_key, method='sha256')
pbk=random.randint(653653,766555455)

db = SQLAlchemy()

class Students(db.Model, UserMixin):
    __name__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2555))
    email = db.Column(db.String(255),unique=True)
    username = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    confirm = db.Column(db.Boolean, default=False, nullable=False)
    confirmed_at = db.Column(db.DateTime)
    gender = db.Column(db.String(30))
    private_key = db.Column(db.String(2555), default=hashed_key)
    public_key = db.Column(db.String(255),default=pbk)
    wallet_balance = db.Column(db.Float(2), default=0.0)
    active=db.Column(db.Boolean,default=False)
    ###Teacher#####
    Qualification = db.Column(db.String(100))
    resume = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    status = db.Column(db.Text)
    website = db.Column(db.String(255))
    rate = db.Column(db.BigInteger, default=0)
    is_instructor = db.Column(db.Boolean, default=False)
    is_student = db.Column(db.Boolean, default=False)


"""
class Teachers(db.Model, UserMixin):
    __name__ = "Teacher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2555))
    email = db.Column(db.String(255),unique=True)
    username=db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    confirm = db.Column(db.Boolean, default=False, nullable=False)
    confirmed_at = db.Column(db.DateTime)
    gender = db.Column(db.String(30))
    Qualification=db.Column(db.String(100))
    resume = db.Column(db.LargeBinary)
    private_key = db.Column(db.String(2555), default=hashed_key)
    wallet_balance = db.Column(db.BigInteger)
    profile_picture = db.Column(db.String(255))
    status=db.Column(db.Text)
    active = db.Column(db.Boolean, default=False)
    website=db.Column(db.String(255))
    public_key = db.Column(db.String(255))
    rate = db.Column(db.BigInteger,default=0)
"""

class Books(db.Model,UserMixin):
    __name__="Books Library"
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255))
    About = db.Column(db.Text)
    Author = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.now())
    image=db.Column(db.String(30000))
    brief=db.Column(db.Text)
    main_book = db.Column(db.LargeBinary)
    price=db.Column(db.BigInteger,default=0)
    book_location = db.Column(db.String(30000))
    private_key=db.Column(db.BigInteger,unique=True)

class Courses(db.Model,UserMixin):
    __name__='Courses'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.now())
    image = db.Column(db.String(30000))
    desriptionsLectures = db.Column(db.Text)
    price = db.Column(db.BigInteger, default=0)
    private_key = db.Column(db.BigInteger, unique=True)

class Lectures (db.Model,UserMixin):
    __name__ = 'Lectures'
    id = db.Column(db.Integer, primary_key=True)
    Topic = db.Column(db.String(255))
    creator=db.Column(db.String(255))
    creator_id = db.Column(db.String(255))

    date_posted = db.Column(db.DateTime, default=datetime.now())
    content = db.Column(db.Text)
    courses_name = db.Column(db.String(255))
    courses_id=db.Column(db.BigInteger)
    private_key = db.Column(db.BigInteger, unique=True)

class settings(db.Model,UserMixin):
    __name__ = 'System Settings'
    id = db.Column(db.Integer, primary_key=True)
    start_exam = db.Column(db.Boolean, default=False)
    exam_url = db.Column(db.String(255))
    maitinance_mode = db.Column(db.Boolean, default=False)
