import curses

import core.backends
from ui.main_menu import MainMenu


def main(stdscr):
    curses.curs_set(0)

    core.backends.check_terminal_size(stdscr)

    menu = MainMenu(stdscr)
    menu.execute()


if __name__ == "__main__":
    curses.wrapper(main)