from flask import Flask, request, jsonify, session
from flask_cors import CORS
from models import db
from models.user import User
from models.Game import Game
from models.Customer import Customer

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GuysGames.db'
db.init_app(app)

@app.route('/games', methods=['POST'])
def add_game():
    try:
        data = request.json
        new_game = Game(
            name=data['name'],
            creator=data['creator'],
            year_published=data['year_published'],
            genre=data['genre'],
            picture_url=data.get('picture_url')
        )
        db.session.add(new_game)
        db.session.commit()
        return jsonify({'message': 'Game added to database.'}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to add game', 'message': str(e)}), 500

@app.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    try:
        game = Game.query.get_or_404(game_id)
        return jsonify({
            'id': game.id,
            'name': game.name,
            'creator': game.creator,
            'year_published': game.year_published,
            'genre': game.genre,
            'picture_url': game.picture_url
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to fetch game details', 'message': str(e)}), 500


@app.route('/games', methods=['GET'])
def get_games():
    try:
        games = Game.query.all()
        games_list = []
        for game in games:
            game_data = {
                'id': game.id,
                'name': game.name,
                'creator': game.creator,
                'year_published': game.year_published,
                'genre': game.genre,
                'picture_url': game.picture_url
            }
            games_list.append(game_data)
        return jsonify({'message': 'Games retrieved successfully', 'games': games_list}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve games', 'message': str(e)}), 500




@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('name')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    print(user)  # Print user object to verify if it exists
    if user and user.password == password:
        return jsonify({
            'message': 'Login successful',
            'user_id': user.id,
            'username': user.username
        }), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    try:
        session.clear()
        return jsonify({'message': 'Logged out'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to logout', 'message': str(e)}), 500

@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    
    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'Game deleted successfully'})

@app.route('/games/<int:game_id>', methods=['PUT'])
def edit_game(game_id):
    try:
        game = Game.query.get_or_404(game_id)
        data = request.json

        game.name = data.get('name', game.name)
        game.creator = data.get('creator', game.creator)
        game.year_published = data.get('year_published', game.year_published)
        game.genre = data.get('genre', game.genre)
        game.picture_url = data.get('picture_url', game.picture_url)

        db.session.commit()
        return jsonify({'message': 'Game updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to update game', 'message': str(e)}), 500
    

@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        customers_list = []
        for customer in customers:
            customers_list.append({
                'id': customer.id,
                'name': customer.name
            })
        return jsonify({'message': 'Customers retrieved successfully', 'customers': customers_list}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve customers', 'message': str(e)}), 500

@app.route('/addCustomer', methods=['POST'])
def add_customer():
    try:
        data = request.json
        new_customer = Customer(name=data['name'])
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer added successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to add customer', 'message': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()


    app.run(debug=True)
