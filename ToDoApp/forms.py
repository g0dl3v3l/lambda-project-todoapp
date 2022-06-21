from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField , DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class EditForm(FlaskForm):
    edittask = StringField()
    editdate = DateField('date' ,format='%Y-%m-%d')
    submit = SubmitField('Edit')

