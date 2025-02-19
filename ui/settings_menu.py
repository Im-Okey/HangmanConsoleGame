from ui.base_menu import BaseMenu


class SettingsMenu(BaseMenu):
    """Меню настроек"""
    def __init__(self, stdscr, settings):
        super().__init__(stdscr, settings.DIFFICULTY_LEVELS)
        self.settings = settings

    def run(self):
        """Запуск меню настроек"""
        choice = self.navigate()
        self.settings.set_difficulty(self.options[choice])