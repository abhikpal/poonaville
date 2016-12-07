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


from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import PasswordField
from wtforms import SelectField
from wtforms.validators import Required
from wtforms.validators import Email
from wtforms.validators import EqualTo

class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[Required()])
    email = StringField("Email", validators=[Email(), Required()])
    password = PasswordField("Enter password", validators=[Required()])
    password_reenter = PasswordField("Re-enter password",
                                    validators=[Required(), EqualTo(password)])
    user_type = SelectField("User type", choices=[
            ('B', "Builder"),
            ('E', "Entrepreneur"),
            ('P', "Punekar")
        ], validators=[Required()])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required()])
    submit = SubmitField("Submit")
