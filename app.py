from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'tembiciS2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jymxtjxbofydcj:70874b0bbca9b68c15ab7c1548707e3188adc091e541563e720d178009de638c@ec2-52-45-14-227.compute-1.amazonaws.com:5432/df3rv39mtth805'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    last_login = db.Column(db.Date)
    token = db.Column(db.String(255))
    phones = db.relationship('Phones', backref='user', lazy=False)


class Phones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ddd = db.Column(db.String(2))
    number = db.Column(db.String(9))


if __name__ == '__main__':
    app.run(debug=True)
