from flask import Flask, render_template, request
from forms import ContactForm
from dns.reversename

app = Flask(__name__)

app.secret_key = 'you are a big donkey | 1492'

@app.route('/')
def lookup():
    form = ContactForm()
    
    if request.method == 'POST':
        return 'Reverse address for IP.'
        
    elif request.method == 'GET':
        return render_template('lookup.html', form=form)
    
