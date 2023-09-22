from lib.Diary_Entry import *


# When a diary entry is created and formatted, 
#the diary entry is returned as a string containg 
#the entry title followed by the diary entry
#contents.

def test_DiaryEntry_format():
    diary_entry = DiaryEntry("Trip to visit grandma", "Today I went to see Grandma.")
    assert diary_entry.format() == "Trip To Visit Grandma: Today I went to see Grandma."


# After a diary entry is created, the number of words in a diary
#entry contents are counted and returned as an integer

def test_DiaryEntry_count_words():
    diary_entry = DiaryEntry("Trip to visit grandma", "Today I went to see Grandma.")
    assert diary_entry.count_words() == 6


# After a diary entry is created, a string containing a rounded up integer representing the estimated time 
#required to read a diary entry is provided, based on words read per minute and 
#the number of words in a diary entry contents.

def test_DiaryEntry_reading_time():
    diary_entry = DiaryEntry("Trip to visit grandma", "Today I went to see Grandma.")
    number_words = diary_entry.count_words()
    assert diary_entry.reading_time(4) == 2


# After a diary entry is created, a chunk of the contents is provided which the user should be able
#to read in the given number of minutes. 

# def test_DiaryEntry_reading_chunk():
#     diary_entry = DiaryEntry("Trip to the zoo", "Today I went to the zoo. There were lots of animals. My favourite animal was the whip-tailed scorpion. It was black.")
#     number_words = diary_entry.count_words()
#     assert diary_entry.reading_chunk(3, 3) == "Today I went to the zoo. There were lots"


#     # When we call the reading_chunk function again, we get the next chunk of the same length of the contents. 
#     assert diary_entry.reading_chunk(3, 3) == "of animals. My favourite animal was the whip-tailed scorpion."

#     # When we call the reading_chunk function enough times that all of the content has been gone through,
#     #it should start again from the beginning.
#     assert diary_entry.reading_chunk(3, 3) == "It was black."
#     assert diary_entry.reading_chunk(3, 3) == "Today I went to the zoo. There were lots"










