from . import db

class Customer(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
