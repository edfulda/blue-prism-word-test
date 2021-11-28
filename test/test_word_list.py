from model.word_list import WordList


def test_file_loading(tmp_path):
    test_file_contents = """the
then
this
that
DOG
cat
HIGH
MiXy
"""
    tmp = tmp_path / "tmpfile.txt"
    tmp.write_text(test_file_contents)

    wl = WordList(4)
    wl.load_from_file(str(tmp))
    # Wordlist should be 6 words long
    assert len(wl) == 5
    assert "dog" not in wl  # Because it's too short
    assert "DOG" not in wl

    assert "HIGH" not in wl
    assert "high" in wl

    assert "MiXy" not in wl
    assert "mixy" in wl


def test_non_four_word_list():
    wl = WordList(6, {"four", "six", "seven", "eleven", "twelve"})
    assert wl == {"eleven", "twelve"}
