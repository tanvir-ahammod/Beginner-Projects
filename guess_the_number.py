import random 

def generate_random_number():
    return random.randrange(1, 100)

def check_guess(guess, number, try_counter):
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {try_counter} tries!")


def run_guess():
    number=generate_random_number()
    print("Computer has generated a random number between 0 and 100. Try to guess it!")
    guess=input("Guess a number between 0 and 100: ")
    try_counter=1
    check_guess(int(guess), number,try_counter)
    while int(guess) != number:
        try_counter += 1
        guess=input("Guess again: ")
        check_guess(int(guess), number,try_counter)

if __name__ == "__main__":
    run_guess()