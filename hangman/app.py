from flask import Flask, render_template, session, request, jsonify
from game_logic import HangmanGame
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

WORDS = ["python", "flask", "hangman", "project", "web"]

def get_game():
    if 'game' not in session:
        word = random.choice(WORDS)
        session['game'] = HangmanGame(word).__dict__
    return HangmanGame.from_dict(session['game'])

@app.route('/')
def index():
    session.clear()  # Start fresh on each visit
    return render_template('index.html')

@app.route('/start')
def start():
    word = random.choice(WORDS)
    game = HangmanGame(word)
    session['game'] = game.__dict__
    return jsonify(game.to_dict())

@app.route('/guess', methods=['POST'])
def guess():
    letter = request.get_json()['letter']
    game = get_game()
    game.guess(letter)
    session['game'] = game.__dict__
    return jsonify(game.to_dict())

if __name__ == '__main__':
    app.run(debug=True)