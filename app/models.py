from app import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):

    ''' A website user. '''

    __tablename__ = 'users'
    name = db.Column(db.String)
    surname = db.Column(db.String)
    usertype = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    confirmation = db.Column(db.Boolean)
    password = db.Column(db.String)
    coins = db.Column(db.Integer, default=0)

    # @hybrid_property
    # def password(self):
    #     return self._password

    # @password.setter
    # def _set_password(self, plaintext):
    #     self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return True if self.password == plaintext else False

    def get_id(self):
        return self.email

class Picture(db.Model):

    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String)
    image_path = db.Column(db.String)
    user_id = db.Column(db.String) 
    verified = db.Column(db.Boolean, unique=False)
    
    def get_id(self):
        return self.id
