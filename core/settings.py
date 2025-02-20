class GameSettings:
    """Настройки игры"""
    DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard", "Expert"]

    WORDS_FILES = {
        "Easy": "data/easy.txt",
        "Medium": "data/medium.txt",
        "Hard": "data/hard.txt",
        "Expert": "data/expert.txt"
    }

    def __init__(self):
        self.difficulty = "Easy"

    def set_difficulty(self, level):
        """Устанановка уровеня сложности игры"""
        if level in self.DIFFICULTY_LEVELS:
            self.difficulty = level

