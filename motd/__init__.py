"""Main Motd Flask App"""
import random

from flask import Flask, abort, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../fortune.db'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String, unique=True, nullable=False)


def get_quotes():
    messages = Message.query.all()
    return [m.quote for m in messages]


def random_quote(messages):
    pick_one = random.randint(0, len(messages) - 1)
    return messages[pick_one]


@app.route('/')
def get_motd():
    try:
        message = random_quote(get_quotes())
    except:
        # Either the db isn't up, or isn't loaded.
        # Either way, no quote today
        abort(503)
    return render_template('index.html', message=message)


def load_quotes(lines):
    existing = get_quotes()
    for line in lines:
        if line in existing:
            continue

        message = Message(quote=line)
        db.session.add(message)
    db.session.commit()
