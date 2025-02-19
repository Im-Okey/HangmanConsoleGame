from ui.base_menu import BaseMenu


class StatisticsMenu(BaseMenu):
    """Меню статистики"""

    def __init__(self, stdscr, stats):
        super().__init__(stdscr, ["Просмотр статистики", "Очистить статистику", "Назад"])
        self.stats = stats

    def run(self):
        """Запуск меню статистики"""
        while True:
            choice = self.navigate()

            if choice == 0:
                self.show_statistics()
            elif choice == 1:
                self.clear_statistics()
            elif choice == 2:
                break

    def show_statistics(self):
        """Отображение статистики"""
        stats = self.stats.get_statistics()

        self.stdscr.clear()
        self.stdscr.addstr(2, 2, f"Общее количество игр: {stats['total']}")
        self.stdscr.addstr(3, 2, f"Выиграно игр: {stats['won']}")
        self.stdscr.addstr(4, 2, f"Проиграно игр: {stats['lost']}")
        self.stdscr.addstr(5, 2, "Статистика по уровням сложности:")

        row = 6
        for difficulty, data in stats['difficulty'].items():
            self.stdscr.addstr(row, 2, f"{difficulty}: {data['won']} выиграно, {data['lost']} проиграно")
            row += 1

        self.stdscr.refresh()
        self.stdscr.getch()

    def clear_statistics(self):
        """Очистка статистики"""
        self.stats.clear_stats()
        self.stdscr.clear()
        self.stdscr.addstr(2, 2, "Статистика очищена!")
        self.stdscr.refresh()
        self.stdscr.getch()
