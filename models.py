from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
   namaUser1 = StringField('Nama user:')
   kataSandi = PasswordField('Kata sandi:')
   submit = SubmitField('Login')
