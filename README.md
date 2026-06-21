# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game is a Streamlit number-guessing app where the player selects a difficulty, submits guesses, and receives higher/lower hints until they find the secret number.
- I found that the difficulty boundaries were reversed for Normal and Hard modes, the New Game reset used a hardcoded 1-100 secret range, and out-of-range guesses were accepted without validation.
- I fixed the bug by moving core game logic into `logic_utils.py`, correcting the difficulty range mapping, adding guess range validation, and keeping the UI state consistent across reruns.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The player chooses a difficulty level from the sidebar and sees the correct range displayed, such as `1 to 20` for Easy.
2. The player enters a guess and clicks `Submit Guess`; the app parses the input and validates that it is a number inside the current range.
3. If the guess is too low, the app returns `Too Low` and asks the player to go higher; if the guess is too high, it returns `Too High` and asks the player to go lower.
4. The score updates after each guess based on the number of attempts and whether the guess was too high, too low, or correct.
5. When the player guesses the secret number, the app displays a win message with the final score and balloons, and the game prevents further play until `New Game` is clicked.

## 🧪 Test Results

```
4 passed
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
