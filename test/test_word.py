import pytest
from model.word import Word
from model.word_list import WordList


@pytest.fixture
def set_up():
    w = Word("four")
    w.validate_word(WordList(4, {"four", "five", "word"}))  # Simple base case test


def test_in_set():
    w = Word("four")
    with pytest.raises(ValueError):
        w.validate_word(WordList(4, {"thee", "then", "this", "that"}))
    w = Word("")
    with pytest.raises(ValueError):
        w.validate_word(WordList(4, {"thee", "then", "this", "that"}))


def test_length():
    w = Word("six")
    with pytest.raises(ValueError):
        w.validate_word(WordList(4, {"six"}))  # Word is in dict but incorrect length

    w = Word("")
    with pytest.raises(ValueError):
        w.validate_word(WordList(4, set()))  # Empty String


def test_non_four_letter():
    w = Word("eleven")
    w.validate_word(WordList(6, {"eleven", "twelve"}))
    with pytest.raises(ValueError):
        w.validate_word(WordList(6, {"four"}))  # Word is in dict but incorrect length


def test_lower_case():
    w = Word("UPPERCASE")
    assert "uppercase" == w

    w = Word("CamelCase")
    assert "camelcase" == w

    w = Word("lowercase")
    assert "lowercase" == w
