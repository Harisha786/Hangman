class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed = []
        self.tries_left = 6
        self.status = 'playing'

    def guess(self, letter):
        if letter in self.guessed or self.status != 'playing':
            return
        self.guessed.append(letter)
        if letter not in self.word:
            self.tries_left -= 1
        if all(l in self.guessed for l in self.word):
            self.status = 'won'
        elif self.tries_left == 0:
            self.status = 'lost'

    def get_display_word(self):
        return ' '.join([l if l in self.guessed else '_' for l in self.word])

    def to_dict(self):
        return {
            'display': self.get_display_word(),
            'tries_left': self.tries_left,
            'guessed': self.guessed,
            'status': self.status,
            'word': self.word if self.status != 'playing' else ''
        }

    @classmethod
    def from_dict(cls, data):
        game = cls(data['word'])
        game.guessed = data['guessed']
        game.tries_left = data['tries_left']
        game.status = data['status']
        return game


