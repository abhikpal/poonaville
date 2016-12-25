#
# Poonaville
# (for the Pune Biennale 2017)
# Copyright (C) 2016  Abhik Pal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from flask import request
from flask import session

from biennale import db
from biennale import socketio
from biennale import active_users

from biennale.database import User

clients = {}

@socketio.on('connect', namespace='/controller')
def user_join():
    email = session['email']
    user = User.query.filter_by(email=email).first()
    payload = {
        'email': user.email,
        'start_coord_x': user.start_coord_x,
        'start_coord_y': user.start_coord_y,
        'meter_life': user.meter_life,
        'meter_status': user.meter_status,
        'meter_karma': user.meter_karma 
    }
    clients[email] = request.sid
    print(payload)
    socketio.emit('user_joined', payload, namespace='/projection')


@socketio.on('disconnect', namespace='/controller')
def user_leave():
    if session['email'] in clients:
        payload = {
            'email': session['email']
        }
        socketio.emit('user_left', payload, namespace='/projection')
        clients.pop(session['email'])
        session.pop('email')


@socketio.on('remove_user', namespace='/projection')
def remove_user(data):
    print(data)
    socketio.emit('remove_user', data, namespace='/controller',
                room=clients[data['email']])

@socketio.on('update_meter', namespace='/projection')
def update_user_meter(data):
    print(data)
    payload = {
        'karma': data['karma'],
        'life': data['life'],
        'status': data['status']
    }
    socketio.emit('update_meter', payload, namespace='/controller',
                room=clients[data['email']])


@socketio.on('movement', namespace='/controller')
def update_user_location(data):
    if session['email'] in clients:
        print(session['email'], data)
        payload = {
            'email': session['email'],
            'x': data['x'],
            'y': data['y']
        }
        socketio.emit('movement', payload, namespace='/projection')
