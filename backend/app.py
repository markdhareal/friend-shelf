from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#DATABASE
db = SQLAlchemy(app)

import routes

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return '<h1>Hello, World</h1>'

if __name__ == '__main__':
    app.run(debug=True)