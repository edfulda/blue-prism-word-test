from model.word_list import WordList
from word_ladder import WordLadder


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
