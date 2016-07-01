from flask import Flask, render_template
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# first line is for home PC, second is for work
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:/personal_site/personal_site/new_db.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Sam/personal_site/personal_site/new_db.db'
db = SQLAlchemy(app)

class List_Cats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    items = db.relationship('list_items', backref='list_cats')
    __tablename__ = "list_cats"
    
    
              
class List_Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    master_list = db.Column(db.Integer, db.ForeignKey('list_cats.id'))
        
        
        
        




@app.route('/')
def home():
    return render_template('hello.html')
    
@app.route('/top-tens/')
def top_ten():
    return render_template('hello.html')
    
@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', show=name)
    
@app.route('/work-with-me/')
def work():
    return render_template('hello.html')
    
@app.route('/fun/')
def fun():
    return render_template('hello.html')
    
@app.route('/things/')
def things():
    return render_template('hello.html')



