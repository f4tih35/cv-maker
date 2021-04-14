from cvmaker import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(30),nullable=False)

    def __repr__(self):
        return f'User: {self.username} | Email: {self.email}'
"""
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
"""


    
