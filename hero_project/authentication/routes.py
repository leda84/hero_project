from flask import Blueprint, render_template, request, redirect, url_for, flash
import flask_wtf
from hero_project.forms import UserLoginForm
from hero_project.models import db,User


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email,password)

            # creating/adding user to database
            user = User(email, password = password)
            db.session.add(user)
            db.session.commit()
            
            flash(f'You have successfully created a user account for {email}. \nWelcome to The Hero Project!', "user-created")
            return redirect(url_for('site.home'))   #maybe change redirect to profile(maybe even pop up option to choose)
    except:
        raise Exception('Invalid Form Data: Please check your info...')

    return render_template('signup.html', form = form)



@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    return render_template('signin.html')