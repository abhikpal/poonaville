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

import sys

from biennale import app
from biennale import db
from biennale import socketio

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'createdb':
            db.create_all()
        elif sys.argv[1] == 'initdb':
            pass
        elif sys.argv[1] == 'reset':
            pass
        elif sys.argv[1] == 'start':
            socketio.run(app, host='0.0.0.0', debug=True)
        else:
            raise IndexError
    except IndexError:
        print("ERROR: Missing/Incorrect parameters")
        print("")
        print("Possible parameters are:")
        print("start \t\t Starts the server.")
        print("createdb \t\t Creates the database.")
        print("initdb \t\t Initializes the database.")
        print("resetdb \t\t Resets the database.")
