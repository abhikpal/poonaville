from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PUNE-biennale-2017'
socketio = SocketIO(app, async_mode=None)

import biennale.routes
import biennale.control
