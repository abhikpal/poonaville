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


import random

from biennale import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    start_coord_x = db.Column(db.Float)
    start_coord_y = db.Column(db.Float)

    meter_life = db.Column(db.Integer)
    meter_status = db.Column(db.Integer)
    meter_karma = db.Column(db.Integer)

    ts_last_logout = db.Column(db.DateTime)
    ts_last_login = db.Column(db.DateTime)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.start_coord_x = random.random()
        self.start_coord_y = random.random()

        self.meter_status = 0
        self.meter_life = 50
        self.meter_karma = 0

    def __repr__(self):
        return '<USER %r>' % self.email
