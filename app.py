import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['JWT_SECRET'] = 'tem'
app.config['PWD_SECRET'] = 'bici'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://yuzfvrasmtufmc:700d87b622e3b1728efa532f95c5600e3a24835cc2d90aa279614a0d98646e4b@ec2-54-210-128-153.compute-1.amazonaws.com:5432/d65mn7rvppp28?sslmode=require'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    last_login = db.Column(db.DateTime)
    token = db.Column(db.String(255))
    phones = db.relationship('Phones', backref='user', lazy=False)


class Phones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ddd = db.Column(db.String(2))
    number = db.Column(db.String(9))


@app.route('/signup', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'] + app.config['PWD_SECRET'], method='sha256')
    new_user = User(name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    for phone in data['phones']:
        user_phone = Phones(user=new_user, ddd=phone['ddd'], number=phone['number'])
        db.session.add(user_phone)
    db.session.commit()
    return jsonify({'message': 'New User Created'}), 201


@app.route('/signin', methods=['POST'])
def update_user():
    return ''


@app.route('/user', methods=['POST'])
def get_all_users():
    users = User.query.all()
    output = []

    for user in users:
        user_phones = []

        for user_phone in user.phones:
            user_phone = {'ddd': user_phone.ddd, 'number': user_phone.number}
            user_phones.append(user_phone)

        user_data = {'id': user.id, 'name': user.name, 'created_at': user.created_at, 'updated_at': user.updated_at,
                     'last_login': user.last_login, 'phones': user_phones}
        output.append(user_data)

    return jsonify({'users': output})


if __name__ == '__main__':
    app.run(debug=True)
