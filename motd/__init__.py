"""Main Motd Flask App"""
from flask import Flask, abort, render_template

from motd.messages import db, get_quotes
from motd.util import random_quote


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../fortune.db'
db.init_app(app)


@app.route('/')
def get_motd():
    try:
        message = random_quote(get_quotes())
    except:
        # Either the db isn't up, or isn't loaded.
        # Either way, no quote today
        abort(503)
    return render_template('index.html', message=message)
