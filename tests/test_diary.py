from lib.diary import *

def test_make_snippet_over_five():
    result = make_snippet("This sentence has more than five words")
    assert result == "This sentence has more than..."

def test_make_snippet_five():
    result2 = make_snippet("This sentence has five words.")
    assert result2 == "This sentence has five words."

def test_make_snippet_four():
    result3 = make_snippet("This is a sentence.")
    assert result3 == "This is a sentence."

def test_make_snippet_one_string_num():
    result4 = make_snippet("5")
    assert result4 == "5"

def test_make_snippet_no_spaces():
    result5 = make_snippet("Thissentencehasmorethanfivewordsbutnobreaks")
    assert result5 == "Thissentencehasmorethanfivewordsbutnobreaks"
    
def test_make_snippet_with_commas():    
    result6 = make_snippet("This,sentence,uses,no,spaces,at,all")
    assert result6 == "This,sentence,uses,no,spaces,at,all"

def test_make_snippet_with_empty_string():
    result7 = make_snippet("")
    assert result7 == ""


