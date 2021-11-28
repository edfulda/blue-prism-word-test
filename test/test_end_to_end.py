from hypothesis import assume, given, strategies as st
from model.word_list import WordList
from word_ladder_cli import main


def test_happy_path():
    wl = WordList(4, {"this", "that", "four", "thin", "thou", "then"})
    assert ["this", "thin"] == main(wl, "this", "thin")  # simple test case
    assert [] == main(wl, "four", "then")  # No results found


def test_case_handling():
    wl = WordList(4, {"this", "that", "four", "thin", "thou", "then"})
    assert ["this", "thin"] == main(wl, "THIS", "ThIN")  # Test case with input words mixed case


def test_blue_prism_examples():
    # Examples from YouTube/Word doc
    wl = WordList(4, {"spin", "spit", "spat", "spot", "span"})
    assert ["spin", "spit", "spot"] == main(wl, "spin", "spot")

    wl = WordList(4)
    wl.load_from_file("./reference/words-english.txt")
    # Note this test is tricky as there are multiple correct answers - so we just check that we
    # have the correct length answer with the correct words at the start and end
    results = main(wl, "hide", "sort")

    assert len(results) == 5
    assert results[0] == "hide"
    assert results[-1] == "sort"


@given(begin=st.text(min_size=4, max_size=4),
       end=st.text(min_size=4, max_size=4),
       words=st.sets(st.text()))
def test_ht_length_four(begin, end, words):
    # Ensure being and end strings in the word list
    full_set = words.union(set([begin])).union(set([end]))
    try:
        wl = WordList(4, full_set)
        main(wl, begin, end)
    except ValueError as err:
        assume("is not in the dictionary" in str(err))


@given(begin=st.text(min_size=8, max_size=8),
       end=st.text(min_size=8, max_size=8),
       words=st.sets(st.text()))
def test_ht_length_eight(begin, end, words):
    # Ensure being and end strings in the word list
    full_set = words.union(set([begin])).union(set([end]))
    try:
        wl = WordList(8, full_set)
        main(wl, begin, end)
    except ValueError as err:
        assume("is not in the dictionary" in str(err))
