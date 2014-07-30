from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(Form):
    ipaddr = TextField('IP Address', validators=[DataRequired()])
    submit = SubmitField('Lookup')
