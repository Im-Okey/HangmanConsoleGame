import json, os, random
from typing import IO

from core.game_difficulty import GameSettings


class WordsManager:
    """Manage files with words"""
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.word = self.load_word(difficulty).upper()

    @staticmethod
    def load_word(difficulty):
        """Loads a word from a file of the appropriate difficulty level"""
        file_path = GameSettings.WORDS_FILES[difficulty]
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Words file {file_path} was not found!")

        with open(file_path, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]

        if not words:
            raise ValueError(f"File {file_path} is empty!")

        return random.choice(words).upper()


class StatsManager:
    """Manage files with statistics"""
    def __init__(self, stats):
        self.stats = stats

    def load_stats(self):
        """Loads game statistics from a file"""
        if os.path.exists(self.stats.stats_file):
            with open(self.stats.stats_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.stats.total_games = data.get('total', 0)
                self.stats.won_games = data.get('won', 0)
                self.stats.lost_games = data.get('lost', 0)
                self.stats.difficulty_stats = data.get('difficulty', self.stats.difficulty_stats)

    def save_stats(self, data):
        """Saves game statistics"""
        try:
            with open(self.stats.stats_file, 'w', encoding='utf-8') as file: # type: IO[str]
                json.dump(data, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            raise f"Stats file {self.stats.stats_file} was not found!"


def check_terminal_size(stdscr):
    """Checks terminal size"""
    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        if max_y < 10 or max_x < 20:
            stdscr.addstr(1, 2, "⚠ Window is too small! ⚠")
            stdscr.addstr(3, 2, "Please resize it to at least 20x10")
            stdscr.addstr(5, 2, "Try to resize it until the game starts....")
            stdscr.refresh()
            stdscr.getch()
        else:
            break