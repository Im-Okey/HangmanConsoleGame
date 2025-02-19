import json
import os
from typing import IO

from core.game import HangmanGame


class GameStatistics:
    """Статистика игры"""

    def __init__(self):
        self.stats_file = 'stats.json'
        self.total_games = 0
        self.won_games = 0
        self.lost_games = 0
        self.difficulty_stats = {difficulty: {'won': 0, 'lost': 0} for difficulty in HangmanGame.WORDS}
        self.load_stats()

    def update_stats(self, game: HangmanGame):
        """Обновление статистики после игры"""
        self.total_games += 1
        if game.is_won():
            self.won_games += 1
            self.difficulty_stats[game.difficulty]['won'] += 1
        else:
            self.lost_games += 1
            self.difficulty_stats[game.difficulty]['lost'] += 1
        self.save_stats()

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

        self.save_stats()

    def load_stats(self):
        """Загрузка статистики из файла"""
        if os.path.exists(self.stats_file):
            with open(self.stats_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.total_games = data.get('total', 0)
                self.won_games = data.get('won', 0)
                self.lost_games = data.get('lost', 0)
                self.difficulty_stats = data.get('difficulty', self.difficulty_stats)

    def save_stats(self):
        """Сохранение статистики в файл"""
        data = {
            'total': self.total_games,
            'won': self.won_games,
            'lost': self.lost_games,
            'difficulty': self.difficulty_stats
        }

        with open(self.stats_file, 'w', encoding='utf-8') as file: # type: IO[str]
            json.dump(data, file, ensure_ascii=False, indent=4)