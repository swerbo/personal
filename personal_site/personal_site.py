from flask import Flask, render_template
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class TopTens(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=True)
        
        
        




@app.route('/')
def home():
    return 'Hello, World!'
    
@app.route('/top-tens/')
def top_ten():
    return 'This is my list of top ten things'
    
@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', show=name)
    
@app.route('/work-with-me/')
def work():
    return render_template('resume.html')
    
@app.route('/fun/')
def fun():
    return 'Fun'
    
@app.route('/things/')
def things():
    return 'Things'



