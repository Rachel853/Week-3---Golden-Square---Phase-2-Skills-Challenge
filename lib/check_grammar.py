def check_grammar(string):
    list_of_punctuation = [".", "!", "?",]
    if any([char in list_of_punctuation for char in string[-1]]):
        return string[0].isupper()

    return False
            

