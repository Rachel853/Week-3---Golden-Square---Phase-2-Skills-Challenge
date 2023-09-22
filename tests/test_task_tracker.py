from lib.task_tracker import *

# Given a string of only '#TODO' returns True
def test_task_tracker_only_TODO_returns_True():
    assert task_tracker('#TODO') == True

# Given a string of only '#todo' returns False
def test_task_tracker_only_todo_returns_False():
    assert task_tracker('#todo') == False

# Given a string of only 'TODO' returns False
def test_task_tracker_only_TODO_no_hash_returns_False():
    assert task_tracker('TODO') == False

# Given a string with '#TODO' at the beginning returns True
def test_task_tracker_TODO_at_beginning_returns_True():
    assert task_tracker('#TODO - eat some cake') == True

# Given a string with '#TODO' at the end returns True
def test_task_tracker_TODO_at_beginning_returns_True():
    assert task_tracker('eat some cake - #TODO') == True

# Given a string with '#TODO' anywhere in it returns True
def test_task_tracker_TODO_anywhere_in_string_returns_True():
    assert task_tracker('for today - #TODO eat some cake') == True

# Given a string with '#TODO', split apart, returns False
def test_task_tracker_TODO_anywhere_in_string_returns_True():
    assert task_tracker('for today - #TO DO eat some cake') == False

# Given a string without '#TODO' anywhere in it, returns False
def test_task_tracker_no_TODO_in_string_returns_True():
    assert task_tracker('for today - eat some cake') == False

# Given a string with '#TODO' preceded and followed immediately by another
# character, returns True
def test_task_tracker_TODO_between_characters_returns_True():
    assert task_tracker('for today -#TODOeat some cake') == True

