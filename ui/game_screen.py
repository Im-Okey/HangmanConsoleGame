import curses
from core.game import HangmanGame


class GameScreen:
    """Экран игры"""
    def __init__(self, stdscr, difficulty):
        self.stdscr = stdscr
        self.game = HangmanGame(difficulty)
        self.start_attempts = self.game.attempts

    def run(self):
        """ИГРА"""
        curses.curs_set(1)
        while not (self.game.is_won() or self.game.is_lost()):
            self.stdscr.clear()
            self.stdscr.addstr(1, 2, f"Слово: {' '.join(self.game.hidden_word)}")
            self.stdscr.addstr(2, 2, f"Попытки: {self.game.attempts}")
            self.stdscr.addstr(3, 2, f"Использованные буквы: {', '.join(self.game.guessed_letters)}")
            self.stdscr.addstr(5, 2, "Введите букву: ")
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

    def show_result(self):
        """Отображение результатов игры"""
        self.stdscr.clear()
        if self.game.is_won():
            self.stdscr.addstr(2, 2, f"Поздравляем! Вы выиграли 🎉")
            self.stdscr.addstr(3, 2, f"Попыток потрачено: {self.start_attempts - self.game.attempts} из {self.start_attempts}")
        else:
            self.stdscr.addstr(2, 2, f"Вы проиграли! Загаданное слово: {self.game.word}")
        self.stdscr.refresh()
        self.stdscr.getch()