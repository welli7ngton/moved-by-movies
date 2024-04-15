import os

from flask import Flask, render_template

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


def create_app(test_config=None):
    # cria e configura o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )

    if test_config is None:
        # carrega a instancia config, se existir, quando não está em cenário
        # de testes
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home():
        return render_template('base.html', title='Home')

    from . import db
    db.init_app(app)

    from . import admin
    app.register_blueprint(admin.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import movies
    app.register_blueprint(movies.bp)

    from . import profile
    app.register_blueprint(profile.bp)

    return app
