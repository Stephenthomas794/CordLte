from flask import Flask, render_template, redirect
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, desc, text
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
socketio = SocketIO(app)

class realestate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zipCodeDB = db.Column(db.Integer, nullable=False)
    housesDB = db.Column(db.Integer, nullable=False)

    def __init__(self, zipCodeDB, housesDB):
        self.zipCodeDB = zipCodeDB
        self.housesDB = housesDB

@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

@app.route("/project1", methods=['POST', 'GET'])
def project1():
    lastUpdate = open("static/project1txt/date.txt","r")
    sqlMax = text('SELECT * FROM realestate ORDER BY housesDB desc LIMIT 0,10')
    results = db.engine.execute(sqlMax)
    d, a = {}, []
    resultproxy = results
    for rowproxy in resultproxy:
        for column, value in rowproxy.items():
            d = {**d, **{column: value}}
        a.append(d)
    return render_template('project1.html', a=a, update=lastUpdate.read())

def send(zipCode, houses):
    arr = [zipCode,houses]
    socketio.emit('message', {'data': arr})
    updateDB(zipCode, houses)
    return

def updateDB(zipCode, houses):
    newZip = realestate(zipCodeDB=zipCode,housesDB=houses)
    try:
        db.session.add(newZip)
        db.session.commit()
        return redirect('/project1')
    except:
        return "Failed"
    return

@app.route("/project2")
def project2():
    return render_template('project2.html')

@socketio.on('connection')
def connection(data):
    print(data)

from projects.project1 import project1_blueprint_factory
this_send = send
project1 = project1_blueprint_factory(this_send)
app.register_blueprint(project1, url_prefix="")
if __name__ == "__main__":
    db.create_all()
    socketio.run(app, host='127.0.0.1')
