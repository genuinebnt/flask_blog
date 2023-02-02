import sqlite3

from flask import g, current_app


def get_db():
    # use the existing db if present else make a new connection
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        g.db.row_factory = sqlite3.Row

    return g.db


def close_db():
    # if no connection then db will be None
    db = g.pop('db', None)

    if db is not None:
        db.close()
