from flask import render_template
from flask import request

from biennale import app
from biennale import socketio

user_element_positions = []

@app.route('/')
def index():
    return render_template("controller.html",
                            ip_address=request.remote_addr)

@app.route('/projection/')
def projection():
    projection_data = {'projection': 'not-implemented'}
    return str(projection_data)
