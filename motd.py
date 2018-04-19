import os
import random

from flask import Flask, render_template


app = Flask(__name__)
messages = [
    'What looks like a cat, flies like a bat, brays like a donkey, and plays like a monkey? A: Nothing.'
]


@app.route('/')
def get_motd():
    pick_one = random.randint(0, len(messages) - 1)
    message = messages[pick_one]
    return render_template('index.html', message=message)


if __name__ == "__main__":
    host = os.getenv('HOST', '0.0.0.0')
    port = os.getenv('PORT', 5000)

    app.run(host, port)