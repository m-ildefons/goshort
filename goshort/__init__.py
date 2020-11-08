#!/usr/bin/env python3
"""
Author: Moritz Röhrich <moritz@ildefons.de>
"""

import os
import flask

from goshort import short, db


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = flask.Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        CMD=["head", "-n", "1"],
        DATABASE=os.path.join(app.instance_path, "goshort.sqlite"),
        URL="http://goshort",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(short.bp)
    app.add_url_rule("/", endpoint="index")

    db.register_app(app)

    return app
