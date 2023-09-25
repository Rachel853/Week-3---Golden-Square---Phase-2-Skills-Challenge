from lib.check_grammar import*

def test_check_grammar():
    result = check_grammar("Dog.")
    assert result == True

def test_check_grammar_no_capital():
    result = check_grammar("dog.")
    assert result == False

def test_check_grammar_no_sentence_end():
    result = check_grammar("Dog")
    assert result == False
 
