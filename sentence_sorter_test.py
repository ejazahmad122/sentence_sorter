import pytest
from sentence_sorter import words_are_valid, sentence_is_valid


def test_words_is_not_valid():
    """test case for Check words length == 0"""
    res = words_are_valid([])
    assert res == False

def test_words_is_valid():
    """test case for Check words length == 0"""
    res = words_are_valid(["hello", 'I', 'am', 'Ejaz'])
    assert res == True

def test_sentence_is_not_valid():
    """test case for check sentence is not contain only alphabets and numbers"""
    res = sentence_is_valid("Hello sir i am Eja of 18 --%")
    assert res == False
    
def test_sentence_is_valid():
    """test case for check sentence contain only alphabets and numbers"""
    res = sentence_is_valid("Hello sir i am Eja of 18")
    assert res == True
