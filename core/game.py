import random


class HangmanGame:
    """Логика игры"""
    WORDS = {
        "Легкий": ["кот"],
        "Средний": ["машина", "компьютер", "монитор"],
        "Трудный": ["энциклопедия", "автомобилист", "гиперпространство"],
        "Эксперт": ["псевдокодификация", "дифференцирование", "электропроводность"]
    }

    def __init__(self, difficulty="Легкий"):
        self.difficulty = difficulty
        self.word = random.choice(self.WORDS[difficulty]).upper()
        self.hidden_word = ["_"] * len(self.word)
        self.attempts = 6
        self.guessed_letters = set()

    def guess_letter(self, letter):
        """Обрабатка попытку угадать букву"""
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
        """Проверка выйграл ли игрок"""
        return "_" not in self.hidden_word

    def is_lost(self):
        """Проверка на проигрыш"""
        return self.attempts <= 0