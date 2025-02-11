from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel = db.Column(db.String(10)) # online or Pos
    total = db.Column(db.Float)
    items = db.Column(db.JSON) # تخزين العناصر ك JSON
    created_at = db.Column(db.DateTime, default=db.func.now())