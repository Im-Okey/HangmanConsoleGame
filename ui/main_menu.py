from ui.base_menu import BaseMenu
from ui.settings_menu import SettingsMenu
from ui.game_screen import GameScreen
from core.settings import GameSettings
from core.game import GameStatistics
from ui.statistics_menu import StatisticsMenu


class MainMenu(BaseMenu):
    """Главное меню"""
    def __init__(self, stdscr):
        super().__init__(stdscr, ["Начать игру", "Настройки", "Статистика", "Выйти"])
        self.settings = GameSettings()
        self.stats = GameStatistics()

    def run(self):
        """Запуск главного меню"""
        while True:
            choice = self.navigate()

            if choice == 0:
                game = GameScreen(self.stdscr, self.settings.difficulty)
                game.run()
            elif choice == 1:
                settings_menu = SettingsMenu(self.stdscr, self.settings)
                settings_menu.run()
            elif choice == 2:
                statistics_menu = StatisticsMenu(self.stdscr, self.stats)
                statistics_menu.run()
            elif choice == 3:
                break
