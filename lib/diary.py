
def make_snippet(string):
    
    words = string.split()
    number_words = len(words)

    if number_words > 5:
        return " ".join(words[:5]) + "..."
    return " ".join(words)
