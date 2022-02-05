#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask import Flask
from flask_migrate import Migrate
from .auth import auth
from .config import DefaultConfig
from .extensions import db, cache, admin, login_manager
from .models import User
from .userland import userland
from .utils import INSTANCE_FOLDER_PATH

DEFAULT_BLUEPRINTS = (
    auth,
    userland,
)


def create_app(config=None, app_name=None, blueprints=None):

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name, instance_path=INSTANCE_FOLDER_PATH, instance_relative_config=True)

    configure_app(app, config)
    configure_blueprints(app, blueprints)
    configure_extensions(app)

    app.config['UPLOADED_IMAGES_DEST'] = os.path.join(os.getcwd(), 'application/static/uploads/images')
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']

    images = UploadSet('images', IMAGES)
    configure_uploads(app, images)
    return app


def configure_app(app, config=None):

    app.config.from_object(DefaultConfig)

    app.config.from_pyfile('production.cfg', silent=True)

    if config:
        app.config.from_object(config)


def configure_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    cache.init_app(app)
    admin.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    login_manager.setup_app(app)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
