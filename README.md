# 🎮 Number Guessing Game

A fun, interactive command-line game built with Python. Test your luck and skills by guessing a random number between 1 and 100!

---

## ✨ Features

- 🎯 **Three Difficulty Levels** - Easy (10 chances), Medium (5 chances), Hard (3 chances)
- ⏱️ **Time Tracking** - See how fast you can guess the number
- 📊 **Smart Hints** - Get feedback if the number is higher or lower
- 🔄 **Replay Mode** - Play multiple rounds without restarting
- ⚠️ **Input Validation** - Error handling for invalid inputs
- 🎨 **Colorful Output** - Emojis and formatted text for better UX

---

## 🚀 Quick Start

### Requirements
- Python 3.6+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/neha169/Number-Guessing-Game.git
   cd Number-Guessing-Game
   ```

2. **Run the game**
   ```bash
   python guessing_game.py
   ```

---

## 🎮 How to Play

1. **Select Difficulty** - Choose between Easy, Medium, or Hard
2. **Guess the Number** - Enter a number between 1 and 100
3. **Get Feedback** - The game tells you if the number is higher or lower
4. **Win or Lose** - Win if you guess correctly within the chances limit
5. **Play Again** - Choose to play another round or exit

---

## 📋 Difficulty Levels

| Level | Chances | Best For |
|-------|---------|----------|
| 🟢 Easy | 10 | Beginners |
| 🟡 Medium | 5 | Intermediate |
| 🔴 Hard | 3 | Experts |

---

## 💡 Game Example

```
===================================
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
===================================

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice (1/2/3): 2

Great! You selected Medium difficulty. You have 5 chances.
Let's start the game!

Enter your guess: 50
❌ Incorrect! The number is greater than 50.
Remaining chances: 4

Enter your guess: 75
❌ Incorrect! The number is less than 75.
Remaining chances: 3

Enter your guess: 62
🎉 Congratulations! You guessed the correct number in 3 attempts.
⏱️ Time taken: 15.34 seconds.

Do you want to play again? (y/n): n
Thanks for playing! Goodbye.
```

---

## 🛠️ Technologies Used

- **Python 3** - Core language
- **random module** - Generate random numbers
- **time module** - Track game duration

---

## 📁 File Structure

```
Number-Guessing-Game/
├── guessing_game.py    # Main game file
└── README.md           # This file
```

---

## 🎯 Game Logic

1. **Generate** - A random number between 1-100
2. **Input** - Player selects difficulty and guesses
3. **Compare** - Check if guess matches the secret number
4. **Feedback** - Tell player if number is higher/lower
5. **Count** - Track attempts and time
6. **Result** - Win or lose based on chances

---

## ⚠️ Notes

- Invalid inputs (non-numbers) are caught and ignored
- Each guess counts as an attempt
- Game timer starts when you begin guessing
- Replaying starts a fresh timer and new random number

---

## 🤝 Contributing

Feel free to improve the game:
- Add score system
- Implement difficulty modes
- Add leaderboard tracking
- Create GUI version with Tkinter

---

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Python. Have fun guessing!** 🎉
