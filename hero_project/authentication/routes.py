from flask import Blueprint, render_template, request, redirect, url_for, flash
import flask_wtf
from werkzeug.security import check_password_hash
from hero_project.forms import UserLoginForm, UserSignupForm, CharacterForm
from hero_project.models import db,User, Character
from flask_login import login_user, logout_user, current_user, login_required


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignupForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            print(first_name, last_name, email, password)

            # creating/adding user to database
            user = User( email,first_name,last_name,  password = password) #changing to this order helped to enter into correct db columns(maybe b/c of init in models)
            db.session.add(user)
            db.session.commit()
            
            flash(f'You have successfully created a user account for {email}. \nWelcome to The Hero Project!', "user-created")
            return redirect(url_for('site.home'))   #maybe change redirect to profile(maybe even pop up option to choose)
    except:
        raise Exception('Invalid Form Data: Please check your info...')

    return render_template('signup.html', form = form)



@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            print(email, password)
            
            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were successfully logged in!', 'auth-success')
                return redirect(url_for('site.profile'))

            else:
                flash('Your email/password is incorrect. Please try again.', 'auth-failed')
                return redirect(url_for('auth.signin'))

    except:
        raise Exception('Invalid Form Data: Please check information entered.')
    return render_template('signin.html', form = form)


@auth.route('/logout')
@login_required     # can't logout if you haven't logged in
def logout():
    logout_user()
    return redirect(url_for('site.home'))

@auth.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    form = CharacterForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data
            alias = form.alias.data
            description = form.description.data
            comics_appeared_in = form.comics_appeared_in.data
            super_power = form.super_power.data
            user_token = current_user.token

            print(name, alias, description, comics_appeared_in, super_power)

            # creating/adding character to database
            character = Character(name, alias, description, comics_appeared_in, super_power, user_token)
            db.session.add(character)
            db.session.commit()
            
            flash(f'You have successfully created a character: {name}!', "character-created")
            return redirect(url_for('site.profile'))
    except:
        raise Exception('Invalid Form Data: Please check your info...')

    return render_template('create.html', form = form)