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

from biennale.database import User
from biennale.database import Level

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
    update_earth_meter()
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
        update_earth_meter()


@socketio.on('remove_user', namespace='/projection')
def remove_user(data):
    print(data)
    player = User.query.filter_by(email=data['email']).first()
    player.start_coord_x = data['locx']
    player.start_coord_y = data['locy']
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.flush()
    socketio.emit('remove_user', data, namespace='/controller',
                room=clients[data['email']])

@socketio.on('update_meter', namespace='/projection')
def update_user_meter(data):
    print(data)
    player = User.query.filter_by(email=data['email']).first()
    player.meter_karma  += int(data['karma'])
    player.meter_life  += int(data['life'])
    player.meter_status  += int(data['status'])
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.flush()
    payload = {
        'karma': player.meter_karma,
        'life': player.meter_life,
        'status': player.meter_status
    }
    update_earth_meter()
    if payload['karma'] == 0:
        socketio.emit('user_left', {'email': player.email}, namespace='/projection')

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


def update_earth_meter():
    earth = Level.query.filter_by(meter_name='Karma').first()

    current_users = {}
    earth.meter_value = 0
    for user in clients:
        foo = User.query.filter_by(email=user).first()
        current_users[foo.email] = {
            'score': foo.meter_status,
            'name': foo.name
        }
        earth.meter_value += foo.meter_karma

    top_users = list(sorted(current_users, key=lambda k: current_users[k]['score']))

    if len(top_users) == 0:
        earth.meter_top_player_1 = "N.A."
        earth.meter_top_player_2 = "N.A."
        earth.meter_top_player_3 = "N.A."
    elif len(top_users) == 1:
        earth.meter_top_player_1 = current_users[top_users[0]]['name']
        earth.meter_top_player_2 = "N.A."
        earth.meter_top_player_3 = "N.A."
    elif len(top_users) == 2:
        earth.meter_top_player_1 = current_users[top_users[0]]['name']
        earth.meter_top_player_2 = current_users[top_users[1]]['name']
        earth.meter_top_player_3 = "N.A."
    else:
        earth.meter_top_player_1 = current_users[top_users[0]]['name']
        earth.meter_top_player_2 = current_users[top_users[1]]['name']
        earth.meter_top_player_3 = current_users[top_users[2]]['name']

    payload = {
        'meter_value': earth.meter_value,
        'top_1': earth.meter_top_player_1,
        'top_2': earth.meter_top_player_2,
        'top_3': earth.meter_top_player_3
    }

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.flush()

    socketio.emit('earth_meter_update', payload, namespace='/projection')
