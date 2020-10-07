#Import packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#Configure the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://fswd:fswd@35.208.39.244:5432/fswd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


#DB Section
db = SQLAlchemy(app)

class Person(db.Model):
	__tablename__='persons'
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(),nullable=False)
	address=db.Column(db.String(),nullable=True)

db.create_all()

person1 = Person(name="Rajeev",address="place")
db.session.add(person1)
db.session.commit()


#Stat the App
@app.route('/')
def index():
	person = Person.query.first()
	return 'hello ' + person.name

