from flask import render_template
from app import app
from app import constants

from app.models import top_holders as top_holders_model
from app.views import top_holders as top_holders_view

@app.route('/')
@app.route('/index')
def index():
    holders = top_holders_model.get_list ("0xb5a5f22694352c15b00323844ad545abb2b11028", 1000)
    holders = top_holders_view.get_list (holders)
    return render_template ('index.html', constants=constants, holders=holders)