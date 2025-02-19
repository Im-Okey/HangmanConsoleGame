import curses
from ui.main_menu import MainMenu


def main(stdscr):
    curses.curs_set(0)
    menu = MainMenu(stdscr)
    menu.run()


if __name__ == "__main__":
    curses.wrapper(main)