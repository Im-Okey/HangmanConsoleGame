# 🎩 Hangman Game

Hangman is a classic game in which the player tries to guess a word by guessing the letters one at a time. If the letter is in the word, it opens. If there is no letter, the player loses the attempt. The game continues until the word is guessed or the attempts run out.
```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

---

## 🚀 Project Description


This project is a modern console version of 'Hangman' with:

✅ **Difficulty selection** (Easy, Medium, Hard, Expert)
✅ **Interactive Terminal Interface (TUI) on curses** 
✅ **Saving statistics of wins and losses** * **Downloading words from files depending on the difficulty level**

---

## 🛠️ Installation and launch

### 1️⃣ Install the dependencies

```sh
pip install uv
uv sync
```

### 2️⃣ Activate the virtual environment

```sh
.venv/Scripts/activate  # Windows
source .venv/bin/activate  # MacOS/Linux
```

### 3️⃣ Launch the game

```sh
python hangman.py
```

---

## 📁 Project structure

```
Hangman/
├── core/                 # Backends
│   ├── game.py           # Main game controller
│   ├── game_statistics.py  # Statistics controller
│   ├── backends.py       # Files management and constraints
│   ├── game_settings.py  # Game settings controller
├── ui/                   # UI
│   ├── base_menu.py      # Base menu class
│   ├── main_menu.py      # Main menu UI
│   ├── statistics_menu.py # Statistics menu UI
│   ├── settings_menu.py  # Settings menu UI
│   ├── game_screen.py    # Game screen UI
├── words/                # Files with words
│   ├── easy.txt
│   ├── medium.txt
│   ├── hard.txt
│   ├── expert.txt
├── stats.json            # File for storing game statistics
├── hangman.py            # Main game launcher
├── pyproject.toml        # Dependencies list
└── README.md             # Project description
```

---

## 🎮 How to play?

Be careful with the language layout of your keyboard. The game support only russian words to play.
The game is not case-insensitive.

1️⃣ Choose the difficulty (Easy, Medium, Hard, Expert)
2️⃣ Enter the letters one at a time, trying to guess the word
3️⃣ If the letter is in the word, it will open
4️⃣ If not, you lose the attempt 
5️⃣ Did you guess the word? 🎉 Victory! 6️⃣ Have you finished trying? Defeat!
7️⃣ The statistics of wins and losses are saved automatically!

---

## 🎮 Controls

Arrow keys (↑ ↓) - Navigate the menu

Enter - Select an option

Letter keys (A-Z) - Guess a letter during the game

---


### 🎩 Have a nice 'Hangman' game! 🕵️‍♂️


---

