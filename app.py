from flask import Flask

from config import DevelopmentConfig
from db import db, migrate, models, api
from search_namespace.views import main_ns, search_ns


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    api.add_namespace(ns=main_ns)
    api.add_namespace(ns=search_ns)

    return app


if __name__ == '__main__':
    app = create_app(DevelopmentConfig)
    app.run()
