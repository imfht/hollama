# flask-sqlalchemy 
from flask_sqlalchemy import SQLAlchemy

import datetime
db = SQLAlchemy()

class RequestLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.Text)
    method = db.Column(db.Text)
    headers = db.Column(db.Text)
    data = db.Column(db.Text)
    remote_addr = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class PathSetting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255))
    method = db.Column(db.String(32))
    sence = db.Column(db.String(32)) # 
    response = db.Column(db.Text)
    response_as_json = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # unique constraint on path-method-sence
    __table_args__ = (
        db.UniqueConstraint('path', 'method', 'sence'),
    )


