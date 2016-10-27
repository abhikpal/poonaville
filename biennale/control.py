from biennale import socketio

@socketio.on('update', namespace='/controller')
def move(message):
    print(message)
    socketio.emit('movement',
                  {'x':message['x'], 'y':message['y']},
                  namespace='/projection')
