from flask import render_template
from . import main
@main.app_errorhandler(404)
def four_ow_four(error):
     '''
     function to render four ow four error page
     '''
     return render_template('fourOwfour.html'),404
