"""Entrypoint to start & run MotD"""
import os

from motd import app
from motd.messages import load_quotes


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
