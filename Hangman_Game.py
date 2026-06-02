import random
words = ['college','school','earth','space','planet']
word =random.choice(words)
guessed_letters = []
chances_left = 6
print("Welcome to Hangman Game!")
print("Guess the word one letter at a time")

while chances_left > 0:
    current_word = ""
    for letter in word:
        if letter in guessed_letters:
            current_word = letter + ""
        else:
            current_word ="_ "
    print("current_word:",current_word)

    if "_" not in current_word:
        print("\nCongratulations! you guessed the word:",word)
        break
    guess = input("enter a letter:")

    if len(guess) !=1 or not guess.isalpha():
        print("plz enter only one alphabet letter")
        continue
    if guess in guessed_letters:
        print("you already guessed this letter,try again")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good job! Letter Found")
    else:
        chances_left -=1
        print("Wrong guess! chances left:",chances_left)
if chances_left == 0:
    print("\nGame Over!")
    print("The Correct word was:",word)

    
