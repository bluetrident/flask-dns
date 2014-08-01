from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired, IPAddress

class ContactForm(Form):
    ipaddr = TextField('IP Address', validators=[DataRequired('IP Address is required.'), IPAddress('Invalid IP Address format.')])
    submit = SubmitField('Lookup')
