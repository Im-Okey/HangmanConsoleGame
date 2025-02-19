from ui.base_menu import BaseMenu
from ui.settings_menu import SettingsMenu
from ui.game_screen import GameScreen
from core.settings import GameSettings


class MainMenu(BaseMenu):
    """Главное меню"""
    def __init__(self, stdscr):
        super().__init__(stdscr, ["Начать игру", "Настройки", "Выйти"])
        self.settings = GameSettings()

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
                break
