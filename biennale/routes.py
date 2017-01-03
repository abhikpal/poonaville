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

from flask import redirect
from flask import request
from flask import render_template
from flask import session
from flask import flash
from flask import g

from biennale import app
from biennale import db
from biennale import socketio
from biennale.control import user_join
from biennale.database import User
from biennale.database import Level
from biennale.forms import LoginForm
from biennale.forms import SignUpForm

@app.route('/', methods=['GET', 'POST'])
def index():
    email = None
    password = None
    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        
        user = User.query.filter_by(email=email).first()
        if user is None:
            flash("You don't have an account yet! Sign Up first")
        elif user.verify_password(password):
            session['email'] = user.email
            return render_template('index.html', async_mode=socketio.async_mode)
        else:
            flash("Invalid password.")

    return render_template('login.html', form=login_form)


@app.route('/projection/')
def projection():
    return render_template('projection.html', async_mode=socketio.async_mode)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    email = None
    password = None
    name = None
    user_type = None
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        email = signup_form.email.data
        password = signup_form.password.data
        name = signup_form.name.data

        try:
            new_user = User(name, email, password)
            new_user.meter_karma = 200
            db.session.add(new_user)
            db.session.commit()
            flash("Account creation successful.")
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            flash("The username already exists!")
        return redirect('/')
        
    return render_template('signup.html', form=signup_form, async_mode=socketio.async_mode)
