from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from os import environ
import redis
from flask_uploads import configure_uploads, IMAGES, UploadSet
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['UPLOADED_IMAGES_DEST'] = os.path.join(os.getcwd(),'cvmaker/static/uploads/images')
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
from cvmaker.models import User

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.isAdmin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.isAdmin

admin = Admin(app, index_view=MyAdminIndexView())
admin.add_view(MyModelView(User, db.session))

from cvmaker import routes
