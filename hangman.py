from string import ascii_lowercase
from words import get_random_word

def get_attempts():
    while True:
        num_attempts = input('How many guesses do you want to have [1-10] ?')
        try: 
            num_attempts= int(num_attempts)
            if 1 < num_attempts and  num_attempts< 25:
                return num_attempts
            else:
                print('{0} is not between 1 and 25'.format(num_attempts))
        except ValueError:
            print('{0} is not between 1 and 25'.format(num_attempts))

def get_word_length ():
    while True:
        min_word_length = input('what is the minimum length of the word you want [4-16]?')
        min_word_length=int(min_word_length)
        try:
            if 4 < min_word_length and min_word_length < 16:
                return min_word_length
            else:
                    print('{0} is not between 4 and 16'.format(min_word_length))
        except ValueError:
            print('{0} is not between 4 and 16'.format(min_word_length))

def get_display_word(word,idxs):
    if len(word)!=len(idxs):
        raise ValueError('Word length and indicies are not the same')
    displayed_word = ''.join([letter if idxs[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip()

def get_next_letter(remaining_letters):
    if len(remaining_letters)==0:
        raise ValueError('There are no more letters remaining')
    while True:
        next_letter = input('choose a letter you want to guess: ').lower()
        if len(next_letter)!=1:
            print('{0} is not a single letter'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{0} has already been guessed'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter

def play_hangman():
    print(' THE GAME IS ABOUT TO BEING ....')
    attempts_remaining = get_attempts()

    print('SELECTING A WORD...')
    word = get_random_word()
    print()

    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False 

    while attempts_remaining>0 and not word_solved:
        print('Word:{0}'.format(get_display_word(word,idxs)))
        print('Attempts reminaing: {0}'.format(attempts_remaining))
        print('Previous Guesses: {0}'.format(' '.join(wrong_letters)))
        
        next_letter = get_next_letter(remaining_letters)

        if next_letter in word:
            print('{0} is in the word'. format(next_letter))
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            print('{0} is not in the word'.format(next_letter))
            attempts_remaining-=1
            wrong_letters.append(next_letter)
        if False not in idxs:
            word_solved = True
            print()


    print('The word is {0}'. format(word))
        
    if word_solved:
        print('Congrats you have won the game')
    else: 
        print('better luck next time loser')

    try_again = input('Would you like to try again? [y/Y]')
    return try_again.lower()=='y'

if __name__ == '__main__':
    while play_hangman():
        print()



