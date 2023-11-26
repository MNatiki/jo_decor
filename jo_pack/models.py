from jo_pack import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Orders(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    choice = db.Column(db.String(1024), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False) 
    address = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"Orders('{self.username}', '{self.choice}', '{self.phone}', '{self.address}')"
