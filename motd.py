import os
import random

from flask import Flask, abort, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fortune.db'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String, unique=True, nullable=False)


@app.route('/')
def get_motd():
    messages = Message.query.all()
    if not messages:
        abort(503)
    pick_one = random.randint(0, len(messages) - 1)
    message = messages[pick_one]
    return render_template('index.html', message=message.quote)


def load_quotes(lines):
    messages = Message.query.all()

    existing = [m.quote for m in messages]
    for line in lines:
        if line in existing:
            continue

        message = Message(quote=line)
        db.session.add(message)
    db.session.commit()


if __name__ == "__main__":
    host = os.getenv('HOST', '0.0.0.0')
    port = os.getenv('PORT', 5000)

    try:
        with open('quotes.txt') as quotes:
            load_quotes(quotes.readlines())
    except:
        # No file, don't care
        pass

    app.run(host, port)
