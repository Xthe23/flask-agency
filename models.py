from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # Adjusted fields to be nullable reflecting their optionality in the form
    resume_filename = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(100), nullable=True) 
    city = db.Column(db.String(100), nullable=True) 
    state = db.Column(db.String(100), nullable=True) 
    zip_code = db.Column(db.String(100), nullable=True)  
    phone = db.Column(db.String(100), nullable=True)  
    # Schedule fields remain unchanged, default=False implies they are optional
    schedule_monday = db.Column(db.Boolean, nullable=False, default=False)
    schedule_tuesday = db.Column(db.Boolean, nullable=False, default=False)
    schedule_wednesday = db.Column(db.Boolean, nullable=False, default=False)
    schedule_thursday = db.Column(db.Boolean, nullable=False, default=False)
    schedule_friday = db.Column(db.Boolean, nullable=False, default=False)
    schedule_saturday = db.Column(db.Boolean, nullable=False, default=False)
    schedule_sunday = db.Column(db.Boolean, nullable=False, default=False)
    start_date = db.Column(db.Time, nullable=True)
    end_date = db.Column(db.Time, nullable=True)
