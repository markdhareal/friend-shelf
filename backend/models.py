from app import db

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    user_session = db.Column(db.String(36), nullable=False)

    def convert_to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'role' : self.role,
            'description' : self.description,
            'gender' : self.gender,
            'imageUrl' : self.image_url
        }