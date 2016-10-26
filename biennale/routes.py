from flask import render_template

from biennale import app
from biennale import socketio

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/projection/')
def projection():
    return render_template('projection.html', async_mode=socketio.async_mode)
