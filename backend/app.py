from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#DATABASE
db = SQLAlchemy(app)

frontend = os.path.join(os.getcwd(), '..', 'frontend')
dist = os.path.join(frontend,'dist')

@app.route('/', defaults={'filename':''})
@app.route('/<path:filename>')
def index(filename):
    if not filename:
        filename = 'index.html'
    return send_from_directory(dist, filename)

import routes

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return '<h1>Hello, World</h1>'

if __name__ == '__main__':
    app.run(debug=True)