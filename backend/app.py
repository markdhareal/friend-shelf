from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# CONFIGURATIONS\
db_path = os.path.join(os.path.expanduser("~"), "myapp", "db.sqlite3")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

os.makedirs(os.path.dirname(db_path), exist_ok=True)

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