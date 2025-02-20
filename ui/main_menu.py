from ui.base_menu import BaseMenu
from ui.settings_menu import SettingsMenu
from ui.game_screen import GameScreen
from core.settings import GameSettings
from core.statistics import GameStatistics
from ui.statistics_menu import StatisticsMenu


class MainMenu(BaseMenu):
    """Represents the main menu"""
    def __init__(self, stdscr):
        super().__init__(stdscr, ["Start new game", "Settings", "Statistics", "Exit"])
        self.settings = GameSettings()
        self.stats = GameStatistics()

    def execute(self):
        """Executes the main menu"""
        while True:
            choice = self.navigate()

            if choice == 0:
                game = GameScreen(self.stdscr, self.settings.difficulty, self.stats)
                game.run()
            elif choice == 1:
                settings_menu = SettingsMenu(self.stdscr, self.settings)
                settings_menu.execute()
            elif choice == 2:
                statistics_menu = StatisticsMenu(self.stdscr, self.stats)
                statistics_menu.execute()
            elif choice == 3:
                break
