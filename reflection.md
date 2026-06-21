# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.


  ## 1. What was broken when you started?

- **What did the game look like the first time you ran it?**
  The game loaded up a structured Streamlit layout with configurable difficulty selectors, status info blocks, and action buttons, but its underlying execution flow and validation algorithms were completely broken. While the user interface visually responded to difficulty adjustments, the variables managing numerical ranges, game resets, and value validations operated independently from one another. This caused misleading UI messages and mathematically impossible game scenarios.

- **List at least two concrete bugs you noticed at the start:**
  1. **Reversal of Difficulty Ranges:** The function defining the boundaries reversed the progression parameters for "Normal" and "Hard" modes, mapping a significantly narrower and easier search pool (1 to 50) to the harder mode.
  2. **Decoupled State Initialization on Reset:** Triggering a fresh session via the "New Game" button forced a static mathematical threshold up to 100, overriding and breaking the bounds for "Easy" difficulty settings completely.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| :--- | :--- | :--- | :--- |
| Select "Hard" difficulty state. | The function `get_range_for_difficulty()` should allocate an expanded or harder numerical pool (e.g., 1 to 100). | The system restricts the boundary scale parameters from 1 to 50, making it narrower and easier than Normal mode. | None (Silent logical flaw) |
| Select **"Easy"** mode and click the **"New Game "** button. | The environment state updates the hidden target number strictly within the Easy parameters of 1 to 20. | The system hardcodes the generation using random.randint(1, 100)`, frequently spawning a target out-of-bounds for the mode. | None (Silent initialization mismatch) |
| Submit an input value of 95 while running on "Easy" mode boundaries. | The input formatting validation utilities should flag that the guess is outside the allowed bounds of 1 to 20. | The system registers the out-of-bounds input as entirely valid, increments the counter, and outputs a generic hint. | None (Missing validation boundary check) |

---

  
## 2. How did you use AI as a teammate?

- I used GitHub Copilot and ChatGPT-style suggestions to help identify refactoring opportunities and to guide debugging.

- Correct AI suggestion:
  - What the AI suggested: Move core game logic out of `app.py` and into `logic_utils.py`, including `parse_guess`, `check_guess`, and `update_score`.
  - Correct or incorrect/misleading: Correct.
  - How it was verified: I verified the result by checking that `app.py` imports those helper functions from `logic_utils.py`, that the game still runs after the refactor, and that `pytest` passed with the updated tests.

- Incorrect/misleading AI suggestion:
  - What the AI suggested: The AI missed the difficulty mapping bug in `get_range_for_difficulty` and did not correct the `Normal`/`Hard` range mismatch on its own.
  - Correct or incorrect/misleading: Incorrect/misleading.
  - How it was verified: I fixed the mapping manually in `logic_utils.py` so `Normal` returns `1, 50` and `Hard` returns `1, 100`, then confirmed the logic by reading the file and validating the game boundaries in the app.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was fixed when the refactored game logic produced the expected behaviour in both code inspection and execution: the difficulty ranges matched the selected mode, the secret number was generated within the active bounds, and out-of-range guesses were rejected.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran `python -m pytest -q` to verify the helper functions in `logic_utils.py`, and all tests passed. I also tested the game manually by selecting `Easy`, clicking `New Game`, and submitting a guess outside `1-20` to confirm the app displayed a range validation warning instead of accepting the input.
- Did AI help you design or understand any tests? How?
  AI helped by suggesting clear helper function boundaries, which made it easier to write focused unit tests for `parse_guess`, `check_guess`, and score updates. That structure also made it simpler to verify fixes quickly with `pytest`.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
