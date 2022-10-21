from flask import Flask, jsonify, request

app = Flask(__name__)

games = [
    {
        'id': 1,
        'title': 'Red Dead Redemption',
        'developer': 'Rockstar'
    },
    {
        'id': 2,
        'title': 'The Witcher 3',
        'developer': 'CD Projekt Red'
    },
    {
        'id': 3,
        'title': 'Ghost of Tsushima',
        'developer': 'Sucker Punch'
    }
]


@app.route('/', methods=['GET'])
def start():
    return jsonify({"welcome": "to Neo's Favorite Games Python API"})


@app.route('/games', methods=['GET'])
def get_games():
    return jsonify(games)


@app.route('/games/<int:id>', methods=['GET'])
def get_game_by_id(id):
    for game in games:
        if game.get('id') == id:
            return jsonify(game)


app.run(port=5000, host='localhost', debug=True)
