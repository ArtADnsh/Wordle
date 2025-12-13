import random
import inflect
import sys

p = inflect.engine()

WORDS = [
    "apple", "crane", "storm", "flame", "brick", "sharp",
    "print", "shout", "trace", "plain", "wheat", "ghost",
    "light", "month", "sword", "chair", "brain", "cloud",
    "dream", "drive", "field", "grass", "heart", "laugh",
    "quick", "river", "sleep", "tiger", "world", "youth"
]

class Letter:
    """
    C: letter is correct and in the right place
    W: letter is in the word but in the wrong place
    N: letter is not in the word
    """
    CORRECT = "C"
    WRONG_SPOT = "W"
    NOT_IN_WORD = "N"


def main():
    word = generate_random_word()

    for i in range(6):
        guess: str = get_input_word(i + 1)
        corrects = guess_checker(word, guess)
        if corrects == 5:
            sys.exit("You guessed correctly!")
    print(f"Sorry, you lost. The word was: {word}")


def generate_random_word() -> str:
    """generates a random word from WORDS list"""
    word:str = random.choice(WORDS)
    return word

def get_input_word(n:int) -> str:
    """gets user's guessed word as input checks whether user's input is 5 chars long or not"""
    if n == 1:
        prompt = "Make your first guess: "
    elif n == 6:
        prompt = "Make your last guess: "
    else:
        remaining = p.number_to_words(6 - n + 1)
        prompt = f"Make your guess: ({remaining} remaining) "

    while True:
        word = input(prompt).strip().lower()

        if len(word) != 5:
            print("Your guess should be 5 characters long. Try again!")
            continue
        if not word.isalpha():
            print("Your guess should only contain letters. Try again!")
            continue

        return word

def guess_checker(word:str, guess:str) -> int:
    """
    gets user's guess and the base word as arguments and checks guess against word
    if corrects variable becomes 5 means that user made the right guess
    """
    corrects = 0 # counts how many letters are correct
    letter_counts = {} # dictionary that counts how many of each letter that is in the correct word too are in the guess
    result = [None] * 5

    for idx in range(5):
        if guess[idx] == word[idx]:
            if guess[idx] in letter_counts:
                letter_counts[guess[idx]] += 1
            else:
                letter_counts[guess[idx]] = 1

            corrects += 1
            result[idx] = Letter.CORRECT

    for idx in range(5):
        if not guess[idx] == word[idx]:
            if guess[idx] in word:

                if guess[idx] in letter_counts:
                    letter_counts[guess[idx]] += 1
                else:
                    letter_counts[guess[idx]] = 1

                if letter_counter(guess[idx], letter_counts[guess[idx]], word):
                    result[idx] = Letter.WRONG_SPOT

                else:
                    result[idx] = Letter.NOT_IN_WORD

            else:
                result[idx] = Letter.NOT_IN_WORD

    print(*result, sep="")
    return corrects

def letter_counter(wanted_letter: str, letter_count: int, word: str) -> bool:
    """
    :param wanted_letter: letter that is in the correct word but in the wrong place
    :param letter_count: how many of that wrong letter found yet
    :param word: correct word
    :return: if there are rooms for the wrong letter, return True
    """
    counter = 0
    for letter in word:
        if letter == wanted_letter:
            counter += 1
    if letter_count <= counter:
        return True
    return False

if __name__ == "__main__":
    main()