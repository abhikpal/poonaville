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
from flask import render_template
from flask import session

from biennale import app
from biennale import socketio
from biennale.forms import LoginForm
from biennale.forms import SignUpForm


@app.route('/')
def index():
    email = None
    password = None
    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        print("Email: %s, Password: %s" % (email, password))
        session['active'] = True

    if session.get('active', False):
        return render_template('index.html', async_mode=socketio.async_mode)
    return render_template('login.html', form=login_form,
                            async_mode=socketio.async_mode)


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
        user_type = signup_form.user_type.data
        print(email, password, name, user_type)
    return render_template('signup.html', form=signup_form, async_mode=socketio.async_mode)


@app.route('/logout/')
def logout():
    session.pop('active')
    return redirect('/')
