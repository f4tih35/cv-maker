#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_login import LoginManager
from flask_admin import Admin, AdminIndexView
from flask_admin.menu import MenuLink


db = SQLAlchemy()
cache = Cache()
login_manager = LoginManager()
login_manager.login_view = "userland.login"
login_manager.login_message = "Please login or signup"


class HomeView(AdminIndexView):
    def is_visible(self):
        return False


admin = Admin(name='cvmaker Admin', template_mode='bootstrap3', index_view=HomeView(name='Home'))
admin.add_link(MenuLink(name='Back to Dashboard', url='/dashboard', icon_type='glyph', icon_value='glyphicon-circle-arrow-left'))
admin.add_link(MenuLink(name='Logout', url='/logout', icon_type='glyph', icon_value='glyphicon-log-out'))
