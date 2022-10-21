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


@app.route('/games')
def get_games():
    return jsonify(games)


app.run(port=5000, host='localhost', debug=True)
