#!/usr/bin/env python3
"""
Author: Moritz Röhrich <moritz@ildefons.de>
"""

import os

import flask

from goshort import db, short


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = flask.Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "goshort.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=False)
    else:
        app.config.update(test_config)

    app.config["SERVER_NAME"] = os.getenv(
        "GOSHORT_URL", app.config["SERVER_NAME"]
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(short.bp)
    app.add_url_rule("/", endpoint="index")

    db.register_app(app)

    return app
