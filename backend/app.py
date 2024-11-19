from flask import Flask, send_from_directory, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import timedelta
import os
import uuid

app = Flask(__name__)
CORS(app, supports_credentials=True)

# CONFIGURATIONS
db_path = os.path.join(os.path.expanduser("~"), "myapp", "db.sqlite3")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SECRET KEY
app.config['SECRET_KEY'] = os.urandom(24)

# COOKIE PARAMETERS FOR COOKIE MANAGEMENT
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

# WILL STORE THE SESSION ID AS AN ENCRYPTED COOKIE
app.config['SESSION_TYPE'] = 'filesystem'

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


@app.before_request
def check_or_create_sessions():
    if 'user_session' not in session:
        session['user_session'] = str(uuid.uuid4())
        session.permanent = True
        print('New Session created')
    else:
        print('Session Found')

@app.route('/api/session', methods=['GET'])
def start_website():
    return jsonify(message='Session is Active')

import routes

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return '<h1>Hello, World</h1>'

if __name__ == '__main__':
    app.run(debug=True)