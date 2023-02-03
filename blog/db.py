import sqlite3, click

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


def close_db(e=None):
    # if no connection then db will be None
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# init_db_command is the function to initialize/reinitialize the database
@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Database initialized')


# Since we are using a factory function we need to pass the app since it is not available globally
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)