"""DB classes/methods for MotD"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String, unique=True, nullable=False)


def get_quotes():
    messages = Message.query.all()
    return [m.quote for m in messages]


def load_quotes(lines):
    existing = get_quotes()
    for line in lines:
        if line in existing:
            continue

        message = Message(quote=line)
        db.session.add(message)
    db.session.commit()
