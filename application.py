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
from biennale.database import Level

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'createdb':
            db.create_all()
            print("DATABASE CREATION SUCCESSFUL.")
        elif sys.argv[1] == 'purgedb':
            db.drop_all()
            print("DATABASE PURGED. ALL DATA HAS BEEN REMOVED.")
        elif sys.argv[1] == 'resetdb':
            db.drop_all()
            db.create_all()
            print("DATABASE RESET SUCCESSFUL")
        elif sys.argv[1] == 'initdb':
            try:
                earth_karma = Level('Karma', 6000)
                db.session.add(earth_karma)
                db.session.commit()
                print("DATABASE INIT SUCCESSFUL")
            except Exception as e:
                db.session.rollback()
                db.session.flush()
                print("DATABASE INIT ABORTED.")
        elif sys.argv[1] == 'start':
            socketio.run(app, host='0.0.0.0', debug=True)
        else:
            raise IndexError
    except IndexError:
        print("ERROR: Missing/Incorrect parameters")
        print("")
        print("Possible parameters are:")
        print("\tstart    - Starts the server.")
        print("\tcreatedb - Creates the database.")
        print("\tinitdb - Creates the database.")
        print("\tpurgedb  - Deletes all information in the database.")
        print("\tresetdb  - Resets the database.")
