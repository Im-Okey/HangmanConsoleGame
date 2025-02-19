class GameSettings:
    """Настройки игры"""
    DIFFICULTY_LEVELS = ["Легкий", "Средний", "Трудный", "Эксперт"]

    def __init__(self):
        self.difficulty = "Легкий"

    def set_difficulty(self, level):
        """Устанановка уровеня сложности игры"""
        if level in self.DIFFICULTY_LEVELS:
            self.difficulty = level