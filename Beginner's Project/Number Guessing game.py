from random import randint


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Set the range for the random number
    lower_limit = 1
    upper_limit = 100
    secret_number = randint(lower_limit, upper_limit)

    # Initialize variables
    attempts = 0
    max_attempts = 10  # You can adjust the number of attempts allowed

    while attempts < max_attempts:
        # Get user's guess
        user_guess = int(input(f"Guess the number between {lower_limit} and {upper_limit}: "))

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts + 1} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        # Increment the number of attempts
        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")


if __name__ == "__main__":
    number_guessing_game()
