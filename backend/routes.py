from app import app, db
from flask import request, jsonify, session
from models import Friend

# GET ALL FRIENDS
@app.route('/api/friends', methods=['GET'])
def get_friends():
    try:

        if 'user_session' not in session:
            return jsonify({'error':'Session not Found'}), 400

        friends = Friend.query.filter_by(user_session=session['user_session']).all()
        result = [friend.convert_to_json() for friend in friends]
        return jsonify(result)
    except Exception as e:
        return jsonify({'error':str(e)}), 500

# CREATE FRIEND
@app.route('/api/friends', methods=['POST'])
def create_friend():
    try:

        if 'user_session' not in session:
            return jsonify({'error':'Session not Found'}), 400

        data = request.json

        required_fields = ['name', 'role', 'description', 'gender']
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify({'error': f'Missing field: {field}'}), 400

        name = data.get('name')
        role = data.get('role')
        description = data.get('description')
        gender = data.get('gender')

        if gender == 'male':
            image_url = f'https://avatar.iran.liara.run/public/boy?username={name}'
        elif gender == 'female':
            image_url = f'https://avatar.iran.liara.run/public/girl?username={name}'
        else:
            image_url = None

        new_friend = Friend(name=name, role=role, description=description, gender=gender, image_url=image_url, user_session=session['user_session'])
        db.session.add(new_friend)
        db.session.commit()

        return jsonify(new_friend.convert_to_json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
    
# DELETE FRIEND
@app.route('/api/friends/<int:id>', methods=['DELETE'])
def delete_friend(id):
    try:
        
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({'error': 'Friend not found'})
        
        db.session.delete(friend)
        db.session.commit()
        return jsonify({'msg':'Friend Deleted'}), 200
        
    except Exception as e:
        db.session.rollback() 
        return jsonify({'error':str(e)}), 500 

# UPDATE FRIEND
@app.route('/api/friends/<int:id>', methods=["PATCH"])
def update_friend(id):
    try:
        
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({'error': 'Friend not found'})
        
        data = request.json

        friend.name = data.get('name', friend.name)
        friend.role = data.get('role', friend.role)
        friend.description = data.get('description', friend.description)
        friend.gender = data.get('gender', friend.gender)

        db.session.commit()
        return jsonify(friend.convert_to_json()), 200

    except Exception as e:

        db.session.rollback()
        return jsonify({'error':str(e)}), 500