from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, abort
from models.users import *
from flask import current_app as app
from werkzeug.utils import secure_filename
import os
from settings.Settings import Setting_Page

dash = Blueprint('dash', __name__)
path2 = 'C:\Users\Harmony\Documents\HarmonyAcademy-master\Harmony\elearning\static\uploads'
picpath = 'C:\Users\Harmony\Documents\HarmonyAcademy-master\Harmony\elearning\static\pics'
path3 = 'http://localhost:5657'

allowed_extensions = set(['pdf'])
allowed_pictures = set(['jpg','png','gif'])
UPLOAD_FOLDER = path2
basedir = os.getcwd()
print(basedir)
#dash.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
def is_instructor_required():
    if current_user.is_instructor == True:
        pass 
    else:
        return abort(404)

def is_student_required():
    if current_user.is_student == True:
        pass 
    else:
        return(abort)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


def allowed_pics(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_pictures


@dash.errorhandler(404)
def error(e):
    return render_template('./error/404.html'), 404


@dash.route('/dashboard')
def dashboard():
    config=settings.query.first()
    if config.maitinance_mode==True:
        msg="<h1>Sorry under maintainance mode!!!</h1>"
        return msg
    else:
        pass
    Setting_Page()
    courses = Courses.query.order_by(Courses.date_posted.desc()).all()
    config=settings.query.first()
    new_test = db.session.query(Students).filter_by(is_instructor=True).count()
    return render_template('./dashboard/home.html', courses=courses, config=config, new_test=new_test)

@dash.route('/bookstore')

def bookstore():
    config=settings.query.first()
    if config.maitinance_mode==True:
        msg="<h1>Sorry under maintainance mode!!!</h1>"
        return msg
    else:
        pass
    Setting_Page()
    books=Books.query.order_by(Books.date_posted.desc()).all()
    new_test = db.session.query(Students).filter_by(is_instructor=True).count()
    config=settings.query.first()
    return render_template('./dashboard/book_gallery.html', books=books,new_test=new_test,config=config)

@dash.route('/payment',methods=['GET','POST'])
def payment():
    config=settings.query.first()
    if config.maitinance_mode==True:
        msg="<h1>Sorry under maintainance mode!!!</h1>"
        return msg
    else:
        pass
    is_instructor_required()
    if request.method=='POST':
        user = Students.query.filter_by(id=current_user.id).first()
        user.wallet_balance +=99.9
        db.session.commit()
        flash('Payments successful')
        return redirect(url_for('dash.dashboard'))
    new_test = db.session.query(Students).filter_by(is_instructor=True).count()

    return render_template('./payments/index.html',new_test=new_test)
    
@dash.route('/gallery')
def course_gallery():
    config=settings.query.first()
    if config.maitinance_mode==True:
        msg="<h1>Sorry under maintainance mode!!!</h1>"
        return msg
    else:
        pass
    new_test = db.session.query(Students).filter_by(is_instructor=True).count()

    return render_template('./dashboard/course_gallery.html',new_test=new_test)


@dash.route('/outline/<course_name>')
def outline(course_name):
    #lectures = Lectures.query.order_by(Lectures.date_posted.desc()).all()
    lectures = Lectures.query.filter_by(courses_name=course_name).all()
    config = settings.query.first()
    new_test = db.session.query(Students).filter_by(is_instructor=True).count()


    return render_template('./dashboard/outline.html',lectures=lectures,config=config,new_test=new_test)

@dash.route('/create_content',methods=['GET','POST'])
def create_content():
    config=settings.query.first()
    if config.maitinance_mode==True:
        msg="<h1>Sorry under maintainance mode!!!</h1>"
        return msg
    else:
        pass
    is_instructor_required()
    if request.method=='POST':
        topic = request.form['topic']
        course = request.form['course']
        main = request.form['main']
        new_lecture = Lectures(Topic=topic, creator=current_user.name, creator_id=current_user.id,
                               content=main, courses_name=course)
        db.session.add(new_lecture)
        db.session.commit()
        flash('Lecture is uploaded')
        return redirect(url_for('dash.create_content'))
    course_lists=Courses.query.all()
    config = settings.query.first()
    new_test = db.session.query(Students).filter_by(is_instructor=True).count()

    return render_template('./dashboard/content/index.html', course_lists=course_lists,config=config,new_test=new_test)

@dash.route('/class/<course_name>')
def classes(course_name):
    classes = Lectures.query.filter_by(courses_name=course_name).all()
    pass
@dash.route('/profile',methods=['GET','POST'])
def profile():
    config=settings.query.first()
    if config.maitinance_mode==True:
        msg="<h1>Sorry under maintainance mode!!!</h1>"
        return msg
    else:
        pass
    if request.method=='POST':
        app.config['UPLOAD_FOLDER'] = picpath
        pics = request.files['pic']
        if pics and allowed_pics(pics.filename):
            filename = secure_filename(pics.filename)

            pics.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            url = "static/pics/"+str(filename)
            user = Students.query.filter_by(id=current_user.id).first()
            user.profile_picture=url
            db.session.commit()
            flash('picture uploaded')
            return redirect(url_for('dash.profile'))
        else:
            flash('sorry file format not allowed')
            return redirect(url_for('dash.profile'))


    config = settings.query.first()
    new_test = db.session.query(Students).filter_by(is_instructor=True).count()

    return render_template('./dashboard/profile/profile.html',config=config,new_test=new_test)



@dash.route('/add_books',methods=['GET','POST'])
def add_books():
    config=settings.query.first()
    if config.maitinance_mode==True:
        msg="<h1>Sorry under maintainance mode!!!</h1>"
        return msg
    else:
        pass
    is_instructor_required()
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method=='POST':
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        title = request.form['title']
        author = request.form['author']
        kit=request.files['file']
        if kit and allowed_file(kit.filename):
            filename = secure_filename(kit.filename)
            
            kit.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            url = "static/uploads/"+str(filename)
            new_kit = Books(Title=title, Author=author, book_location=url)
            db.session.add(new_kit)
            db.session.commit()
            flash('kit uploaded thanks for contributing to the community')
            return redirect(url_for('dash.add_books'))
        else:
            flash('sorry file format not allowed')
            return redirect(url_for('dash.add_books'))
    config = settings.query.first()
    new_test = db.session.query(Students).filter_by(is_instructor=True).count()

    return render_template('./dashboard/upload/index.html',config=config,new_test=new_test)

