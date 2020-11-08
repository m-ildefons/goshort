#!/usr/bin/env python3
"""
Author: Moritz Röhrich <moritz@ildefons.de>
"""


import random
import string
import validators
import flask

from goshort import db


bp = flask.Blueprint("short", __name__)


@bp.route("/", methods=("GET", "POST"))
def index():
    """
    Blueprint route for /.
    """
    return redirect(None)


@bp.route("/<string:name>", methods=("GET", "POST"))
def redirect(name):
    """
    Blueprint route for /<string:name>.
    """
    if name == "favicon.ico":
        return ""

    code = 200
    malformed_url = False

    database = db.get_db()
    row = database.execute('SELECT long_uri '
                           'FROM urls WHERE ident = ?',
                           (name, )).fetchone()

    if not row:
        if flask.request.method == 'POST':
            long_uri = flask.request.form['url']
            if validators.url(long_uri):
                name = _insert(long_uri, name)
                return "%s/%s" % (flask.current_app.config['URL'], name)
            code = 400
            malformed_url = True

        golinks = database.execute('SELECT u.* from urls u '
                                   'WHERE u.id IN '
                                   '(SELECT h.uri_id from home h)').fetchall()
        return flask.make_response(flask.render_template(
                                       'short/index.html',
                                       golinks=golinks,
                                       malformed_url=malformed_url),
                                   code)

    long_uri = dict(row)['long_uri']
    return flask.redirect(long_uri, code=301)


def _insert(long_uri, ident):
    save_home = False
    if not ident:
        ident = _random_string()
    else:
        save_home = True

    if long_uri:
        print('%s %s' % (ident, long_uri))

        database = db.get_db()
        cursor = database.execute('INSERT INTO urls (ident, long_uri) '
                                  'VALUES (?, ?)',
                                  (ident, long_uri))
        if save_home:
            database.execute('INSERT INTO home (display_name, uri_id) '
                             'VALUES (?, ?)',
                             (ident, cursor.lastrowid))
        database.commit()
    return ident


def _random_string(size=8, char_selection=string.ascii_lowercase):
    _string = ''
    database = db.get_db()
    while not _string or database.execute('SELECT ident FROM urls '
                                          'WHERE ident = ?',
                                          (_string, )).fetchall():
        _string = ''.join(random.choice(char_selection) for i in range(size))

    return _string
