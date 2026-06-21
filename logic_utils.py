def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Corrected difficulty ranges and moved this logic here with AI pair-programming.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    # FIX: Refactored parsing from `app.py` into this helper with AI help (handles floats->int).
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def validate_guess_range(guess: int, low: int, high: int):
    """Validate that a numeric guess falls within the current difficulty bounds.

    Returns: (ok: bool, error_message: str | None)
    """
    # FIX: Added range validation to prevent out-of-bounds guesses; added after AI-assisted debugging.
    try:
        if guess < low or guess > high:
            return False, f"Guess must be between {low} and {high}."
    except TypeError:
        return False, "Invalid guess type."

    return True, None


def check_guess(guess, secret):
    # FIX: Fixed hint direction messages here with AI; ensures messages match numeric relation.
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        # Guess is higher than the secret; prompt user to guess lower
        return "Too High", "📉 Go LOWER!"

    # Guess is lower than the secret; prompt user to guess higher
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    # FIX: Scoring logic moved from `app.py` and verified with AI-driven tests.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
