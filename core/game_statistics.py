from core.backends import StatsManager
from core.game import HangmanGame
from core.game_difficulty import GameSettings


class GameStatistics:
    """Represents the logic of game statistics"""

    def __init__(self):
        self.stats_file = 'stats.json'
        self.total_games = 0
        self.won_games = 0
        self.lost_games = 0
        self.difficulty_stats = {difficulty: {'won': 0, 'lost': 0} for difficulty in GameSettings.WORDS_FILES}
        self.stats_manager = StatsManager(self)
        self.load_stats()

    def update_stats(self, game: HangmanGame):
        """Updates game statistics"""
        self.total_games += 1
        if game.is_won():
            self.won_games += 1
            self.difficulty_stats[game.difficulty]['won'] += 1
        else:
            self.lost_games += 1
            self.difficulty_stats[game.difficulty]['lost'] += 1
        self.save_stats()

    def get_stats(self):
        """Returns game statistics"""
        return {
            'total': self.total_games,
            'won': self.won_games,
            'lost': self.lost_games,
            'difficulty': self.difficulty_stats
        }

    def clear_stats(self):
        """Clears game statistics"""
        self.total_games, self.won_games, self.lost_games  = 0, 0, 0
        self.difficulty_stats = {difficulty: {'won': 0, 'lost': 0} for difficulty in GameSettings.WORDS_FILES}
        self.save_stats()

    def load_stats(self):
        """Loads game statistics"""
        self.stats_manager.load_stats()

    def save_stats(self):
        """Saves game statistics"""
        data = {
            'total': self.total_games,
            'won': self.won_games,
            'lost': self.lost_games,
            'difficulty': self.difficulty_stats
        }

        self.stats_manager.save_stats(data)
