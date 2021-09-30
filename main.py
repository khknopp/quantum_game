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

@app.route('/')
def main():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template('index.html')



# -------^ROUTES^-------

if __name__ == '__main__':
    app.run(debug=True)
