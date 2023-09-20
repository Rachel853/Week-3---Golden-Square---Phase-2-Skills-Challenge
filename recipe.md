{{PROBLEM}} Function Design Recipe
Copy this into a recipe.md in your project and fill it out.

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.


<!-- As a user
So that I can manage my time
I want to see an estimate of reading time for a text, 
assuming that I can read 200 words a minute. -->


2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.


# EXAMPLE
<!-- def reading_time(text):
    """"Calculates time required to read text assuming reading speed of 200 words a minute""""

    Parameters: 
        text: string of text to be read 
            e.g. "In the beginning the universe was created. This has widely been considered a bad move."

    Returns: 
        string - hours (if applicable) and minutes calculated to read text.
            e.g. "1 hour and 20 minutes."

    Side effects:
        This function doesn't print anything
         -->


def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.


3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

<!-- """
Given a string of 200 words, it will return "1 minute."
""""

"""
Given a string of 12400 words (200 wpm * 62 minutes), it will return "One hour and 2 minutes."
""""

"""
Given an empty string, it will throw an error: "No text provided.".
"""

"""
Given a string with only whitespace, it will throw an error: "No text provided."
"""

"""
Given a None value it throws an error: "No text provided."
"""
-->


"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
Ensure all test function names are unique, otherwise pytest will ignore them!