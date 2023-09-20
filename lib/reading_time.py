def reading_time(string):
    wpm = 2
    words = string.split()
    number_words = len(words)    
    minutes = number_words // wpm
    hours = minutes // 60
    if minutes > 1 or minutes == 0:
        if minutes >= 60:
            
            extra_minutes = minutes % 60
            return f"{hours} hour {extra_minutes} minutes."
    return f"{minutes} minutes."



