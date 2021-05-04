"""
File: hangman.py
Name: Mike
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    pre-condition: start the game and try to guess out the answer
    post-condition: (1)find out the correct answer and win the game
                    (2)unable to find the correct answer and lose the game
    """
    correct = random_word()
    correct2 = ''
    for i in range(len(correct)):
        correct2 += '-'
    j = 0
    lives_left = N_TURNS - j
    print('The word looks like: ' + str(correct2))
    print('You have ' + str(lives_left) + ' guesses left.')
    while not correct2.isalpha():
        if lives_left != 0:
            guess = input('Your guess: ')
            if guess.isalpha() or not ' ':
                if len(guess) == 1:
                    guess = guess.upper()
                    if guess in correct:
                        print('You are correct!')
                        correct2 = replace(correct, guess, correct2)
                        print('The word looks like: ' + str(correct2))
                        print('You have ' + str(lives_left) + ' guesses left.')
                    else:
                        print('There is no ' + str(guess) + "'s in the word.")
                        lives_left -= 1
                        print('The word looks like: ' + str(correct2))
                        print('You have ' + str(lives_left) + ' guesses left.')
                else:
                    print('illegal format')
            else:
                print('illegal format')
        else:
            print('You are completely hung :(')
            print('The word was: ' + str(correct))
            break
    if correct2.isalpha():
        print('You win!!')
        print('The word was: ' + str(correct2))


def replace(correct, guess, correct2):
    """
    Find out if your guess is in the correct answer or not, if yes, put it into your answer
    """
    ans = ''
    i = 0
    for ch in correct:
        if guess == ch:
            ans += correct[i]
        else:
            ans += correct2[i]
        i += 1
    # for i in range(len(correct)):
    #     if guess == correct[i]:
    #         ans += guess
    #     else:
    #         ans += correct2[i]
    return ans


def random_word():
    """
    To select a random word from the word list
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
