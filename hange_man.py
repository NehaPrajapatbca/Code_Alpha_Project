import random

def hangman():
    words = ["python", "intern", "codealpha", "project", "hangman"]
    word = random.choice(words).lower()
    guessed = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        display = [letter if letter in guessed else "_" for letter in word]
        print("Word:", " ".join(display))

        if "_" not in display:
            print(" You won! The word was:", word)
            return

        guess = input("Enter a letter: ").lower()
        if guess in guessed:
            print(" Already guessed!")
        elif guess in word:
            guessed.append(guess)
            print(" Correct!")
        else:
            attempts -= 1
            guessed.append(guess)
            print(" Wrong! Attempts left:", attempts)

    print("You lost! The word was:", word)

if __name__ == "__main__":
    hangman()
