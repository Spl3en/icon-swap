from flask import render_template
from app import app
from app import constants
import json

from app.models import top_holders as top_holders_model
from app.views import top_holders as top_holders_view
from app.models import swap_status as swap_status_model
from app.views import swap_status as swap_status_view

@app.route('/')
@app.route('/index')
def index():
    holders = top_holders_model.get_list ("0xb5a5f22694352c15b00323844ad545abb2b11028", 200)
    holders = top_holders_view.get_list (holders)
    return render_template ('index.html', constants=constants, holders=holders)

@app.route('/swap/<string:address>')
def swap (address):
    status = swap_status_model.get_status (address)
    status = swap_status_view.get_status (status)
    result = json.dumps({'address' : address, 'status' : status})
    return result