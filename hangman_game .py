import random

words = ["python", "apple", "computer", "school", "chatbot"]

secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_guesses:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct Guess!")
    else:
        incorrect_guesses += 1
        print("Wrong Guess!")
        print("Remaining Attempts:", max_guesses - incorrect_guesses)

if incorrect_guesses == max_guesses:
    print("\nGame Over!")
    print("The word was:", secret_word)
