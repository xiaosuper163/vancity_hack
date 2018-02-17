from app import db
from app import models
db.drop_all()
db.create_all()
