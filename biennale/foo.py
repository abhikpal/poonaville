from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PUNE-biennale-2017'
socketio = SocketIO(app, async_mode=None)

@app.route('/')
def index():
    return render_template('index.html',
                            async_mode=socketio.async_mode)

@app.route('/projection/')
def projection():
    return render_template('projection.html',
                            async_mode=socketio.async_mode)

@socketio.on('update', namespace='/controller')
def move(message):
    print(message)
    socketio.emit('movement',
                  {'data': message['cmd']},
                  namespace='/projection')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
