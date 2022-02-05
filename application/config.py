#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from application.utils import INSTANCE_FOLDER_PATH


class BaseConfig(object):
    PROJECT = "cvmaker"
    PROJECT_NAME = "cvmaker"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    BASE_URL = "https://cvmaker.domain"
    ADMIN_EMAILS = ['admin@cvmaker.domain']
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'always-change-this-secret-key-with-random-alpha-nums'


class DefaultConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + INSTANCE_FOLDER_PATH + '/db.sqlite'
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60
