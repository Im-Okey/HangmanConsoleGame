from core.backends import WordsManager


class HangmanGame:
    """Represents the game logic"""

    def __init__(self, difficulty="Easy"):
        self.difficulty = difficulty
        self.word = WordsManager(difficulty).load_word(difficulty)
        self.hidden_word = ["_"] * len(self.word)
        self.attempts = 6
        self.guessed_letters = set()

    def guess_letter(self, letter):
        """Handles user input"""
        if letter in self.guessed_letters:
            return False

        self.guessed_letters.add(letter)

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.hidden_word[i] = letter
            return True
        else:
            self.attempts -= 1
            return False

    def is_won(self):
        """Checks if the player has won"""
        return "_" not in self.hidden_word

    def is_lost(self):
        """Checks if the player has lost"""
        return self.attempts <= 0
