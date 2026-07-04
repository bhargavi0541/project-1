number=27
attempts=0
guess=1
lives=5
print("Welcome to the Number Guessing Game.")
print("I am thinking of a secret number between 1 and 50. You need to Guess It.")
if guess>=1 and guess<=50:
    while attempts<5 or guess==number:
        guess= int(input("Enter your Guess: "))
        if number>guess:
            print("The secret number is greater than " ,guess)
            attempts= attempts+1
            lives= lives-1
            print("Remaining Guesses:")
            for i in range (1,lives+1):
                print("♡")
        elif number<guess:
            print("The secret number is lesser than ",guess) 
            attempts= attempts+1
            lives= lives-1
            print("Remaining Guesses:")
            for i in range (1,lives+1):
                print("♡")
        else:  
            print("Congratualations! You WIN. You have accurately guessed my Number.")
else:
    "Wrong Choice! You need to guess a number between 1 and 50."    