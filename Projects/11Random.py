print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
guess = int(input("Enter your guess: "))
if guess < 1 or guess > 100:
    print("Please guess a number that is between 1 and 100.")
else:
     if guess < number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed the number.)   