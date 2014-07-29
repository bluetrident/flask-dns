from flask.ext.wtf import Form, TextField, SubmitField

class ContactForm(Form):
    ipaddr = TextField("ipaddr")
    submit = SubmitField("Lookup")
