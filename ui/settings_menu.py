from ui.base_menu import BaseMenu


class SettingsMenu(BaseMenu):
    """Represents settings menu"""
    def __init__(self, stdscr, settings):
        super().__init__(stdscr, settings.DIFFICULTY_LEVELS)
        self.settings = settings

    def execute(self):
        """Executes settings menu"""
        choice = self.navigate()
        self.settings.set_difficulty(self.options[choice])