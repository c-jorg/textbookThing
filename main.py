from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Rewards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reward_name = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user= db.relationship('User', backref='rewards')

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

class RewardSchema(ma.ModelSchema):
    class Meta:
        model = Rewards

@app.route('/')
def index():
    one_user = User.query.first()
    user_schema = UserSchema()
    output = user_schema.dump(one_user).data
    return jsonify({'user' : output})

if __name__ == '__main__':
    app.run(debug=True)