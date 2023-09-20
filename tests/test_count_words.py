from lib.count_words import *

def test_count_words_multiple_words():
    result = count_words("This should return four.")
    assert result == 4

def test_count_words_empty_string():
    result = count_words("")
    assert result == 0

def test_count_words_start_with_space():
    result = count_words(" This starts with a space.")
    assert result == 5

def test_count_words_multiple_sentences():
    result = count_words("This is the first sentence. This is the second sentence.")
    assert result == 10

def test_count_words_one_character():
    result = count_words("a")
    assert result == 1