from lib.count_words import *

def test_count_words_returns_number_of_words():
    actual = count_words("hey how are you?")
    expected = 4

    assert actual == expected