# words = ["apple", "banana", "chocolate", "dog", "elephant", "frog"]

from tracemalloc import start


def print_upper_words(words): 
    """prints the words of the list "words" in upper case
        example) print_upper_words(["hi", "how", "are", "you"])
        HI 
        HOW 
        ARE 
        YOU
    """
    for word in words:
        print(word.upper())
    
def print_words_just_e(words): 
    """prints words of the list "words" that start with e
        example) print_upper_words(["dog", "elephant", "frog"])
        elephant
    """
    for word in words: # iterating through each word in the words list
        if word.startswith("e" or "E"): # if the word starts with e (true)
            print(word.upper()) # we print that word(s)
    

def print_words_just_letter(words, starts_with="e"): 
    """prints words of the list "words" that start with the letter the user inputs but default to e if no input is made
        example) print_upper_words(["dog", "elephant", "frog"], "f")
        frog
    """
    for word in words: # iterating through each word in the words list
        if word.startswith(starts_with): # if the word starts with the param letter that we put in
             print(word.upper()) # we print that word(s)