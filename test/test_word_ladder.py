from hypothesis import given, strategies as st
from model.word_list import WordList
from model.word_ladder import WordLadder


def test_get_next_words():

    wl = WordLadder("heart", "charl", WordList(5, {"heart", "charl", "hhart", "hharl", "zzzzz"}))

    assert {"hhart"} == wl.get_next_words("heart")

    assert {"hharl"} == wl.get_next_words("hhart")

    assert {"charl"} == wl.get_next_words("hharl")

    assert set() == wl.get_next_words("zzzzz")  # Should return no results


def test_calculate_route():
    wl = WordLadder("heart", "chart", WordList(5, {"heart", "charl", "hhart", "hharl"}))
    assert [] == wl.calculate_route()  # "chart" not in the dict

    wl = WordLadder("heart", "charl", WordList(5, {"heart", "charl", "hhart", "hharl"}))

    assert ["heart", "hhart", "hharl", "charl"] == wl.calculate_route()


@given(start=st.text(min_size=1), target=st.text(min_size=1), words=st.sets(st.text(min_size=1)))
def test_ht_get_next_words(start, target, words):
    # Got to ensure start and target are the same length:
    if len(start) > len(target):
        start = start[0:len(target)]
    else:
        target = target[0:len(start)]
    words = [w for w in words if len(w) == len(start)]
    wl = WordLadder(start, target, WordList(len(start), words))

    for w in words:
        wl.get_next_words(w)


@given(start=st.text(min_size=1), target=st.text(min_size=1), words=st.sets(st.text(min_size=1)))
def test_ht_calculate_route(start, target, words):
    # Got to ensure start and target are the same length:
    if len(start) > len(target):
        start = start[0:len(target)]
    else:
        target = target[0:len(start)]

    wl = WordLadder(start, target, WordList(len(start), words))

    wl.calculate_route()
