import curses
from core.game import HangmanGame


class GameScreen:
    """Represent the game process screen"""
    def __init__(self, stdscr, difficulty, stats):
        self.stdscr = stdscr
        self.game = HangmanGame(difficulty)
        self.start_attempts = self.game.attempts
        self.stats = stats

    def run(self):
        """Run the game"""
        curses.curs_set(1)
        while not (self.game.is_won() or self.game.is_lost()):
            self.stdscr.clear()
            self.stdscr.addstr(1, 2, f"Hidden word: {' '.join(self.game.hidden_word)}")
            self.stdscr.addstr(2, 2, f"Attempts: {self.game.attempts}")
            self.stdscr.addstr(3, 2, f"Used letters: {', '.join(self.game.guessed_letters)}")
            self.stdscr.addstr(5, 2, "Input letter: ")
            self.stdscr.refresh()

            key = self.stdscr.getch()
            if (97 <= key <= 122) or (1072 <= key <= 1103):
                letter = chr(key)
            elif (65 <= key <= 90) or (1040 <= key <= 1071):
                letter = chr(key).lower()
            else:
                continue

            self.game.guess_letter(letter.upper())

        self.show_result()
        self.stats.update_stats(self.game)

    def show_result(self):
        """Display the game results"""
        self.stdscr.clear()
        if self.game.is_won():
            self.stdscr.addstr(2, 2, f"Congratulations! You won! 🎉")
            self.stdscr.addstr(3, 2, f"Attempts spent: {self.start_attempts - self.game.attempts} out of {self.start_attempts}")
        else:
            self.stdscr.addstr(2, 2, f"You lost! The hidden word was: {self.game.word}")
        self.stdscr.refresh()
        self.stdscr.getch()
