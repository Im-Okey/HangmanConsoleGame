import curses

from ui.base_menu import BaseMenu
from core.backends import check_terminal_size


class StatisticsMenu(BaseMenu):
    """Represents statistics menu"""

    def __init__(self, stdscr, stats):
        super().__init__(stdscr, ["Show stats", "Clear stats", "Back"])
        self.stats = stats

    def execute(self):
        """Executes statistics menu"""
        while True:
            choice = self.navigate()

            if choice == 0:
                try:
                    self.show_statistics()
                except curses.error:
                    pass
                finally:
                    check_terminal_size(self.stdscr)
            elif choice == 1:
                self.stats.clear_stats()
                self.stdscr.clear()
                self.stdscr.addstr(1, 2, "Statistics was cleared!")
                self.stdscr.addstr(3, 2, "Press Enter to continue...")
                self.stdscr.refresh()
                self.stdscr.getch()
            elif choice == 2:
                break

    def show_statistics(self):
        """Displays statistics"""
        stats = self.stats.get_stats()

        self.stdscr.clear()
        self.stdscr.addstr(1, 2, f"Total games played: {stats['total']}")
        self.stdscr.addstr(3, 2, f"Games won: {stats['won']}")
        self.stdscr.addstr(4, 2, f"Games lost: {stats['lost']}")
        self.stdscr.addstr(6, 2, "Statistics on difficulty levels")

        row = 7
        for difficulty, data in stats['difficulty'].items():
            self.stdscr.addstr(row, 2, f"{difficulty}: {data['won']} won, {data['lost']} lost")
            row += 1

        self.stdscr.addstr(row + 1, 2, "Press Enter to continue...")
        self.stdscr.refresh()
        self.stdscr.getch()
