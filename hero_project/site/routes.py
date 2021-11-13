from flask import Blueprint, render_template

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
def profile():
    return render_template('.profile.html')

