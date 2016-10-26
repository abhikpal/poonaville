from biennale import socketio

@socketio.on('update', namespace='/controller')
def move(message):
    print(message)
    socketio.emit('movement',
                  {'data': message['cmd']},
                  namespace='/projection')
