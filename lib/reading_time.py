def reading_time(string):
    wpm = 200
    words = string.split()
    number_words = len(words)
    
    minutes = number_words // wpm

    return f"{minutes} minute."



