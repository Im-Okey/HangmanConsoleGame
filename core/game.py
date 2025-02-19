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


class GameStatistics:
    """Статистика игры"""

    def __init__(self):
        self.total_games = 0
        self.won_games = 0
        self.lost_games = 0
        self.difficulty_stats = {difficulty: {'won': 0, 'lost': 0} for difficulty in HangmanGame.WORDS}

    def update_stats(self, game: HangmanGame):
        """Обновление статистики после игры"""
        self.total_games += 1
        if game.is_won():
            self.won_games += 1
            self.difficulty_stats[game.difficulty]['won'] += 1
        else:
            self.lost_games += 1
            self.difficulty_stats[game.difficulty]['lost'] += 1

    def get_statistics(self):
        return {
            'total': self.total_games,
            'won': self.won_games,
            'lost': self.lost_games,
            'difficulty': self.difficulty_stats
        }

    def clear_stats(self):
        """Очистка статистики"""
        self.total_games = 0
        self.won_games = 0
        self.lost_games = 0
        self.difficulty_stats = {difficulty: {'won': 0, 'lost': 0} for difficulty in HangmanGame.WORDS}
