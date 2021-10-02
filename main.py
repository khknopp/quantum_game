import os
import os.path
import random
import re
import sys
import json
import string
from datetime import datetime
from flask import Flask, flash, render_template, redirect, request, url_for, jsonify, session, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.reflection import Inspector
import levels

# -----------^IMPORTS^---------------

app = Flask(__name__)
app.secret_key = 'ljrgregjorrejrekirew9843j'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'



# -------------^CONFIGS^-------------

db = SQLAlchemy(app)

class Level(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Qubits = db.Column(db.Integer, nullable=False)
    Monsters = db.Column(db.Integer, nullable=False)
    Gates = db.Column(db.String(50))
    Description = db.Column(db.String(100), nullable=False)
    Success = db.Column(db.String(50), nullable=False)
    Failure = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Level('{self.Id}', '{self.Qubits}', '{self.Monsters}', '{self.Gates}', '{self.Description}', '{self.Success}','{self.Failure}')"

db.create_all()

# -----------------^DATABASE^-----------------------

# Defining the levels:
if(Level.query.all() == []):
    levels.createAllLevels(db, Level)


# ------------------^FUNCTIONS^------------------------------

@app.route('/logout')
def logout():
    session['level'] = 0
    return redirect(url_for('introduction'))

@app.route('/')
def main():
    if(session['level'] == 0):
        return redirect(url_for('introduction'))
    else:
        return redirect(url_for('description'))

###### Introduction ######
@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/introduction_next')
def introduction_text():
    session['level'] = 1
    return redirect(url_for('description'))


###### Description ######
@app.route('/description')
def description():
    if(session['level'] == 0 or session['level'] == None):
        return redirect(url_for('introduction'))
    description = Level.query.filter_by(Id=session['level']).first().Description
    return render_template('description.html', level=session['level'], description=description)

@app.route('/description_next')
def description_next():
    if(session['level'] == 0 or session['level'] == None):
        return redirect(url_for('introduction'))
    return redirect(url_for('level'))


###### Level ######
@app.route('/level')
def level():
    return render_template('level.html')

###### Level success ######
@app.route('/success')
def success():
    session['level'] += 1
    return render_template('success.html')

@app.route('/success_next')
def success_next():
    return redirect(url_for('description'))

###### Level failure ######
@app.route('/failure')
def failure():
    return render_template('failure.html')

@app.route('/failure_next')
def failure_next():
    return redirect(url_for('description'))


# -------^ROUTES^-------

if __name__ == '__main__':
    app.run(debug=True)