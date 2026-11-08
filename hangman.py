import random

words = ["apple","banana","kiwi","strawberry","mango","papaya",
         "dragonfruit","grapes","watermelon","tomato","blueberry",
         "raspberry","orange","blackberry","plum","cherry","pineapple"]

guessed = []
wrong_guesses = 0

word = random.choice(words)

hangman = [
    """
     ------
          |
          |
          |
          |
    =========
    """,
    """
     ------
      |   |
          |
          |
          |
    =========
    """,
    """
     ------
      |   |
      O   |
          |
          |
    =========
    """,
    """
     ------
      |   |
      O   |
      |   |
          |
    =========
    """,
    """
     ------
      |   |
      O   |
     /|\\  |
          |
    =========
    """,
    """
     ------
      |   |
      O   |
     /|\\  |
     /    |
    =========
    """,
    """
     ------
      |   |
      O   |
     /|\\  |
     / \\  |
    =========
    """
]

max_attempts = len(hangman) - 1

print("Welcome to Hangman!")
print("Hint: The word is a fruit.\n")

while wrong_guesses < max_attempts : 
    
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + ""
        else:
            display += "_ "

    print(hangman[wrong_guesses])
    print("Word:", display)
    print()

    if "_ " not in display:
        print("CONGRATULATIONS! You won!")
        print("The word was: ", word,"\n")
        break
    
    guess = input("Enter a letter: ").lower()
    print("\n")
    check = 'abcdefghijklmnopqrstuvwxyz'

    if (guess not in check) or (len(guess) != 1) or not (guess.isalpha()):
        print("Please enter one alphabet.\n")
        continue

    if guess in guessed :
        print("You have already guessed this letter.\n")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")

else:
    print(hangman[-1])
    print("Game Over !!!")
    print("The fruit was: ", word)
    