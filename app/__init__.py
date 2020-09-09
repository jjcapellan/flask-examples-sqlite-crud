import os
from flask import Flask
from app.db import init_db


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['DATABASE'] = os.path.join(app.instance_path, 'db.sqlite')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        init_db()

    from . import crud
    app.register_blueprint(crud.bp)

    return app