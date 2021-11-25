import pytest
from model.word import Word


@pytest.fixture
def setUp():
    # Test cases will rely on 4 letter words. Patch it in just in case it's been changed
    Word.WORD_LENGTH = 4
    w = Word("four")
    w.validate_word({"four", "five", "word"})  # Simple base case test


def test_in_set():
    w = Word("four")
    with pytest.raises(ValueError):
        w.validate_word({"thee", "then", "this", "that"})
    w = Word("")
    with pytest.raises(ValueError):
        w.validate_word({"thee", "then", "this", "that"})


def test_length():
    w = Word("six")
    with pytest.raises(ValueError):
        w.validate_word({"six"})  # Word is in dict but incorrect length

    w = Word("")
    with pytest.raises(ValueError):
        w.validate_word(set())  # Empty String


def test_lower_case():
    w = Word("UPPERCASE")
    assert "uppercase" == w

    w = Word("CamelCase")
    assert "camelcase" == w

    w = Word("lowercase")
    assert "lowercase" == w
