from . import db
from datetime import datetime

class Block(db.Model):
    __tablename__ = 'blockchain'

    id = db.Column(db.Integer, primary_key=True)
    previous_hash = db.Column(db.String(255))
    current_hash = db.Column(db.String(255), nullable=False)
    degree_id = db.Column(db.Integer, db.ForeignKey('degrees.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    nonce = db.Column(db.Integer, nullable=False)
    approved = db.Column(db.Boolean, default=False)

    approvals = db.relationship('Approval', backref='block', lazy=True)

    def __repr__(self):
        return f'<Block {self.current_hash[:10]}...>'
