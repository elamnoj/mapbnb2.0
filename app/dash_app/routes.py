from .import dash_app as chi
from flask_login import login_required


@login_required
@chi.route('/chi-map')
def chi_map():
    return chi_map
