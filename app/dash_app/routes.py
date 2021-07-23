from .import app as chi_map
from flask_login import login_required

@login_required
@chi_map.route('/chi-map')
def chi_map():
    return chi_map
