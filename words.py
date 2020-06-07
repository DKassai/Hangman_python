import random

words= 'words.txt'

def get_random_word():
    num_words_processed = 0
    curr_word = None
    with open(words,'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            
            num_words_processed+=1
            if random.randint(1,num_words_processed)==1:
                curr_word = word
    return curr_word