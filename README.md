# HANGMAN_GAME


This Python code is a simple implementation of the Hangman game where the computer selects a random word from a predefined list, and the player has to guess the word letter by letter. Here's a breakdown of how the code works:

choose_word() function:

This function selects a random word from the word_list which contains words like "apple", "banana", etc.
It uses the random.choice() function from the random module to randomly select a word from the list.
The selected word is returned to the caller.

display_word(word, guessed_letters) function:

This function takes two parameters: word, which is the randomly chosen word, and guessed_letters, which is a set containing the letters that the player has guessed so far.
It iterates over each letter in the word.
If the letter has been guessed (i.e., it is in the guessed_letters set), it adds the letter to the display string.
If the letter has not been guessed, it adds an underscore _ to the display string.
The function returns the display string, which represents the word with guessed letters revealed and unguessed letters hidden.

play_hangman() function:

This function is the main function that orchestrates the Hangman game.
It starts by calling choose_word() to select a random word.
It initializes an empty set guessed_letters to keep track of the letters guessed by the player and sets the number of tries to 6.
Inside a while loop, the game continues as long as the player has remaining tries (tries > 0).
In each iteration of the loop:
It displays the current state of the word using display_word().
It checks if the player has guessed all the letters in the word. If so, it prints a congratulatory message and breaks out of the loop.
It prompts the player to guess a letter.
It validates the player's input to ensure it is a single letter.
It checks if the guessed letter is in the word. If not, it decrements the tries count.
If the player runs out of tries, it prints a message indicating that the player has lost and reveals the word.
The game ends when the player either guesses the word correctly or runs out of tries.
This code provides a simple and interactive Hangman game experience for the player.
