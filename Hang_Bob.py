"""
Hang Bob: Guess the Word!
Author: Quinton Lin
"""

__author__ = "Quinton Lin"


import random
from constant_strings import wordlist, stages


def rand_word():
    """Get a random word from wordlist."""

    word = random.choice(wordlist)
    return word.upper()


PROMPT = "Enter either a letter or a word, no numbers or any other characters: "


def get_input():
    """Get guess from user and check if it's all alphabets."""

    guess = input("\n\nPlease enter your guess! " + PROMPT)
    guess = guess.upper()
    valid_guess = False
    while valid_guess == False:
        for i in guess:
            if ord(i) < 65 or ord(i) > 90:
                guess = input("\nInvalid input! " + PROMPT)
                guess = guess.upper()
                break
        valid_guess = True
    return guess


def word_completion(guessed_letters: list, word: str, completion: list) -> list:
    """Replace "_" with guessed letters that are in the word in the correct spot.

    >>> word_completion(["a","b","c"], "apple")
    ['a', '_', '_', '_', '_']
    >>> word_completion([],"bag")
    ['_', '_', '_']
    """

    for i in range(len(word)):
        for letter in range(len(guessed_letters)):
            if guessed_letters[letter] == word[i]:
                completion[i] = guessed_letters[letter]
    return completion


def letter_guess(guess: str, guessed_letters: list, word: str, attempts: int):
    """Check if the guess is guessed already and whether or not it's in the word.
    
    >>> letter_guess("a", ["a","b"], "computer", 2)
    2
    >>> letter_guess("t", ["a", "e", "g"], "apple", 3)
    4
    """

    if guess in guessed_letters:
        print("\nYou have guessed this letter already!")
    elif guess in word:
        print("\nCorrect! This letter is in the word!")
        guessed_letters.append(guess)
    elif guess not in word:
        print("\nYour guess was not in the word! Please try again!")
        attempts += 1
        guessed_letters.append(guess)
    return attempts


def word_guess(guessed_words: list, guess: str, word: str, guessed: bool, attempts: int, completion: list):
    """Check if the guess matches the word.
    >>> word_guess(["guess","day"], "sweets", "apple", False, 0, ["_", "_", "_", "_", "_"])
    False, 1, [""]
    >>> word_guess([""], "hat", "hat", False, 3, ["_","A", "_"])
    True, 3, ["H", "A", "T"]
    """

    if guess in guessed_words:
        print("\nYou have guessed this word already! Please try again!")
    elif guess == word:
        completion = ("{}".format(guess.upper()))
        guessed_words.append(guess)
        guessed = True
    else:
        print("\nYou have guessed the word incorrectly!")
        attempts += 1
        guessed_words.append(guess)

    return guessed, attempts, completion


def completion_check(completion: list) -> bool:
    """Check if all of the letters of the word have been guessed.
    >>> completion_check(["_", "_", "_"])
    False
    >>> completion_check(["H", "A", "T"])
    True
    """

    if "_" not in completion:
        print("\nYou have guessed the word! Congrats!")
        return True
    else:
        return False


def display(attempts: int, completion: list, guessed_letters: list, guessed_words: list):
    """Display the Hang Bob and missing words."""

    print(stages[attempts])
    for i in completion:
        print(i, end=" ")
    print("\n\nGuessed letters: ", end="")
    for letter in guessed_letters:
        print(letter, end=" ")
    print("\nGuessed words: ", end="")
    for word in guessed_words:
        print(word, end=" ")


def game():
    """Run the Hang Bob game"""

    word = rand_word()
    guessed_letters = []
    guessed_words = []
    completion = []
    for i in range(len(word)):
        completion.append("_")
    guessed = False
    attempts = 0
    completion = word_completion(guessed_letters, word, completion)
    display(attempts, completion, guessed_letters, guessed_words)
    while not guessed and attempts < 6:
        guess = get_input()
        # Run if user inputs a letter
        if len(guess) == 1:
            attempts = letter_guess(guess, guessed_letters, word, attempts)
            completion = word_completion(guessed_letters, word, completion)
        # Run if user inputs a word
        if len(guess) > 1:
            guessed, attempts, completion = word_guess(guessed_words, guess, word, guessed, attempts, completion)
        guessed = completion_check(completion)
        display(attempts, completion, guessed_letters, guessed_words)
    if not guessed:
        print("\n\nYou did not guess the word! The word was {}".format(word))


def main():
    """Run the main program, check if user wants to play Hang Bob and runs the game function"""

    start = input("Would you like to play Hang Bob? Please enter (y)es or (n)o: ").upper()
    while start != "N" and start != "NO":
        if start == "Y" or start == "YES":
            game()
            start = input("\n\nWould you like to play again? Please enter (y)es or (n)o: ").upper()
        else:
            start = input("Invalid input! Please enter (y)es or (n)o: ").upper()
    print("Have a nice day!")


if __name__ == "__main__":
    main()
