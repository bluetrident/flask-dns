from flask import Flask, render_template, request, flash
from forms import ContactForm
import dns.reversename
import socket
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = 'you are a big donkey | 1492'


@app.route('/', methods=['GET', 'POST'])
def lookup():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            revname = str(dns.reversename.from_address(request.form['ipaddr'])) + "<br />" + socket.getfqdn(request.form['ipaddr'])
            return revname
        else:
            return render_template('lookup.html', form=form)
                 
    elif request.method == 'GET':
        return render_template('lookup.html', form=form)
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
