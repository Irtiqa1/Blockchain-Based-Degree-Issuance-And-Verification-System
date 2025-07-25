from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(30), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)# Renamed and updated length
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def set_password(self, password):
      self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)
    
    