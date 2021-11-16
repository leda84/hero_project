from flask import Blueprint, render_template
from flask_login.utils import login_required


"""
    Note that in the code below,
    some arguments are specifies when creating Bluepront objects.
    The first argument, 'site' is the Blueprint's name,
    which flask uses for routing.

    The second argument, __name__, is the Blueprint's import name,
    which flask uses to locate the Blueprint's resources
"""

site = Blueprint('site', __name__, template_folder = 'site_templates')

#creating routes
#will be the location/home/ first thing our visitors will see
@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

# moved to auth routes instead
# @site.route('/create')
# @login_required
# def create():
#     form = CharacterForm()
#     try:
#         if request.method == 'POST' and form.validate_on_submit():
#             name = form.name.data
#             alias = form.alias.data
#             description = form.description.data
#             comics_appeared_in = form.comics_appeared_in.data
#             super_power = form.super_power.data

#             print(name, alias, description, comics_appeared_in, super_power)

#             # creating/adding user to database
#             character = Character(name, alias, description, comics_appeared_in, super_power)
#             db.session.add(character)
#             db.session.commit()
            
#             flash(f'You have successfully created a character: {name}!', "character-created")
#             return redirect(url_for('site.profile'))
#     except:
#         raise Exception('Invalid Form Data: Please check your info...')

#     return render_template('create.html', form = form)