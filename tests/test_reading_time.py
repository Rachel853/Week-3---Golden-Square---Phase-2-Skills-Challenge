import pytest 
from lib.reading_time import *

# """
# Given a string of 200 words, it will return "1 minute."
# """"
two_hundred = "In a quiet corner of a quaint village, time seems to slow down. The cobblestone streets wind their way through picturesque cottages adorned with colorful flowers. A gentle breeze carries the scent of freshly cut grass, and the distant chirping of birds fills the air. Life here revolves around simplicity and community. Neighbors know each other by name, and a friendly wave is the customary greeting. The local market is a hub of activity, where farmers proudly display their fresh produce, and artisans showcase their crafts. As the seasons change, so do the village's landscapes. Spring blankets the meadows with wildflowers, while summer brings lazy afternoons by the tranquil river. In autumn, the trees become a tapestry of vibrant hues, and winter turns the village into a snow-covered wonderland. Amidst the rustic charm, there's a sense of harmony with nature. The village is a refuge from the hustle and bustle of modern life, where the ticking of the clock is less urgent, and people savor the simple pleasures of each day. In this idyllic setting, one can't help but reflect on the beauty of a life well-lived, where time is measured in moments, and the bonds of friendship and community"
over_hour = "In a quiet corner of a quaint village, time seems to slow down. The cobblestone streets wind their way through picturesque cottages adorned with colorful flowers. A gentle breeze carries the scent of freshly cut grass, and the distant chirping of birds fills the air. Life here revolves around simplicity and community. Neighbors know each other by name, and a friendly wave is the customary greeting. The local market is a hub of activity, where farmers proudly display their fresh produce, and artisans showcase their crafts. As the seasons change, so do the village's landscapes. Spring blankets the meadows with wildflowers, while summer brings lazy afternoons by the tranquil river. In autumn, the trees become a tapestry of vibrant hues, and winter turns the"

def test_reading_time_one_min():
    assert reading_time("the dog") == "1 minutes."

def test_reading_time_ten_mins():
    assert reading_time("the dog the dog the dog the dog the dog the dog the dog the dog the dog the dog") == "10 minutes."


# """
# Given a string of 124 words (200 wpm * 62 minutes), it will return "One hour and 2 minutes."
# """"
def test_reading_time_over_hour():
    assert reading_time(over_hour) == "1 hour 2 minutes."

# """
# Given a string of 12400 words (200 wpm * 62 minutes), it will return "One hour and 2 minutes."
# """"

# """
# Given a string of 70874 words ((200 wpm * (60 minutes * 5)) + (200 * 54 minutes)) + 79 words, it will return "5 hours and 54 minutes."
# """

# """
# Given an empty string, it will throw an error: "No text provided.".
# """
def test_reading_time_empty_string():
    assert reading_time("") == "0 minutes."

# """
# Given a string with only whitespace, it will throw an error: "No text provided."
# """

# """
# Given a None value it throws an error: "No text provided."
# """


