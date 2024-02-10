import random

def choose_word():
    word_list = ["apple", "banana", "orange", "grape", "pear"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    tries = int(input("enter number of tries:"))

    print("Welcome to Hangman!")
    print("Guess the word. You have", tries,"tries.")

    while tries > 0:
        print("\nWord:", display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            tries -= 1
            print("Incorrect guess. You have", tries, "tries left.")

    else:
        print("Sorry, you ran out of tries. The word was:", word)

if __name__ == "__main__":
    play_hangman()
