#!/usr/bin/env python3
"""
Author: Moritz Röhrich <moritz@ildefons.de>
"""


import sqlite3
import click
import flask


def init_db():
    """
    Database initialization.
    """
    database = get_db()

    with flask.current_app.open_resource('schema.sql') as schema:
        database.executescript(schema.read().decode('utf-8'))


@click.command('init-db')
@flask.cli.with_appcontext
def init_db_command():
    """
    Database initialization command binding for flask.
    """
    init_db()
    click.echo('Database initialized empty.')


def get_db():
    """
    Get Database - returns a database handle.
    """
    if 'db' not in flask.g:
        flask.g.db = sqlite3.connect(
                flask.current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES)
        flask.g.db.row_factory = sqlite3.Row
    return flask.g.db


def close_db(error=None):
    """
    Close Database - properly closes the database on programm termination.
    """
    database = flask.g.pop('db', None)

    if database is not None:
        database.close()

    if error:
        print(error)


def register_app(app):
    """
    Close Database binding to application termination event.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
