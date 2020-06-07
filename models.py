import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

# database_path = os.environ['DATABASE_URL']
# if not database_path:
#     database_name = "travelapi"
#     database_path = 'postgresql://postgres@localhost:5432/travelapi'

database_name = "travelapi"
database_path = 'postgresql://postgres@localhost:5432/travelapi'

db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


# Models
class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    travels = db.relationship('Travel', backref='guide', lazy=True)

    def __repr__(self):
        return f'<Guide: {self.name} {self.surname}>'

    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'phone': self.phone,
        }


class Travel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    content = db.Column(db.Text, nullable=False)
    guide_id = db.Column(db.Integer, db.ForeignKey('guide.id'), nullable=False)

    def __repr__(self):
        return f'<Travel: {self.title}>'

    def __init__(self, title, content, guide_id):
        self.title = title,
        self.content = content,
        self.guide_id = guide_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'guide_id': self.guide_id,
            'guide_name': self.guide.name,
        }
