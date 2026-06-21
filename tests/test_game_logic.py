from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should return a win tuple.
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be Too High with the correct lower message.
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be Too Low with the correct higher message.
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_specific_easy_hint_direction():
    # Targeted regression test: secret 5 and guess 1 should tell the player to go higher.
    result = check_guess(1, 5)
    assert result == ("Too Low", "📈 Go HIGHER!")
