from core.game import HangmanGame


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