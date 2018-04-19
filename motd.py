import os

from flask import Flask


app = Flask(__name__)

@app.route('/')
def get_motd():
    return "Hello, world!"


if __name__ == "__main__":
    host = os.getenv('HOST', '0.0.0.0')
    port = os.getenv('PORT', 5000)

    app.run(host, port)