import random

# Computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

# Loop until the user guesses correctly
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if guess < 1 or guess > 10:
            print("Please enter a number within the range 1 to 10.")
        elif guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        elif:
            print("Congratulations! You guessed it!")
        else:
            print("It took you {attempts} attempts.")
        
            break
    