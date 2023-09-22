from lib.grammar_stats import *

def test_can_create_grammar_stats_object():
    stats = GrammarStats()
    assert True

def test_check_a_grammatically_correct_string_passes():
    stats = GrammarStats()
    result = stats.check("Hello, world!")
    assert result == True

def test_check_no_capital_first_letter_fails():
    stats = GrammarStats()
    result = stats.check("hello, world!")
    assert result == False

def test_check_no_end_sentence_punctuation_fails():
    stats = GrammarStats()
    result = stats.check("Hello, world")
    assert result == False

def test_percentage_good_zero_returned_if_no_tests_run():
    stats = GrammarStats()
    result = stats.percentage_good()
    assert result == 0

def test_percentage_good_rounded_up_67_returned_for_two_out_of_three_passes():
    stats = GrammarStats()
    stats.check("This doesn't end with a sentence ending punctuation mark:")
    stats.check("A correct sentence?")
    stats.check("Let's try another one.")
    result = stats.percentage_good()
    assert result == 67

def test_percentage_good_rounded_down_33_returned_for_one_out_of_three_passes():
    stats = GrammarStats()
    stats.check("This doesn't end with a sentence ending punctuation mark:")
    stats.check("A correct sentence?")
    stats.check("i don't think this one is correct!")
    result = stats.percentage_good()
    assert result == 33