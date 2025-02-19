import curses


class BaseMenu:
    """Базовый класс для всех меню"""
    def __init__(self, stdscr, options):
        self.stdscr = stdscr
        self.options = options
        self.current_row = 0

    def draw_menu(self):
        """Отображение меню"""
        self.stdscr.clear()
        for i, option in enumerate(self.options):
            if i == self.current_row:
                self.stdscr.addstr(i + 1, 2, f"> {option} <", curses.A_REVERSE)
            else:
                self.stdscr.addstr(i + 1, 2, f"  {option}  ")
        self.stdscr.refresh()

    def navigate(self):
        """Логика перемещения курсора"""
        while True:
            self.draw_menu()
            key = self.stdscr.getch()

            if key == curses.KEY_UP and self.current_row > 0:
                self.current_row -= 1
            elif key == curses.KEY_DOWN and self.current_row < len(self.options) - 1:
                self.current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return self.current_row