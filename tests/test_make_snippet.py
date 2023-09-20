from lib.make_snippet import *

def test_make_snippet_returns_string():
    actual = make_snippet("hello")
    expected = 'hello'

    assert actual == expected

def test_make_snippet_returns_five_words():
    actual = make_snippet("one two three four five")
    expected = "one two three four five"

    assert actual == expected

def test_make_snippet_returns_six_words_and_three_dots():
    actual = make_snippet("one two three four five six")
    expected = "one two three four five..."

    assert actual == expected