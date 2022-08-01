import re

def sentence_sorter():
    """Sort the sentence alphabetically order"""
    sentence = input("Enter a sentence : ")         #Taking a sentence as input
        
    if sentence_is_valid(sentence):                 #Check sentence is contain only alphabets and numbers
        words = [word.lower() for word in sentence.split()]
        if words_are_valid(words):                  #Check list contain atleast length > 0
            sorted_sentence = sorted(words)

            print('Sorted list of words are : \n', sorted_sentence)
        else:
            print('Please enter a valid sentence!!')
    else:
        print('You have entered an invalid sentence !!!')


def words_are_valid(words):
    """Check words leng in a sentence is greater then 0

    Args:
        words (list): list of words that are in sentence

    Returns:
        bool: if word length is grater than 0 then True
    """
    if len(words) > 0:
        return True
    return False

def sentence_is_valid(sentence):
    """Check sentence is contain only alphabets and numbers

    Args:
        words (str): sentence

    Returns:
        bool: if sentence is valid then True
    """
    return bool(re.match("^[A-Za-z0-9 ]*$", sentence))



sentence_sorter()