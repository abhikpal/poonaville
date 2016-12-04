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

from biennale import socketio

@socketio.on('update', namespace='/controller')
def move(message):
    # print(message)
    # print(request.remote_addr)
    socketio.emit('movement',
                    {
                        'x':message['x'],
                        'y':message['y'],
                        'client':request.remote_addr
                    },
                    namespace='/projection')
