from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField , DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo


#User registration form
class UserForm(FlaskForm):
    username = StringField('username')
    email = StringField('email')
    password = PasswordField('password')
    submit=SubmitField('Submit')




class EditForm(FlaskForm):
    edittask = StringField()
    editdate = DateField('date' ,format='%Y-%m-%d')
    sortdate  =DateField('date' ,format='%Y-%m-%d')
    submit = SubmitField('Update')

