# 1) Import the `random` module to let the computer make a random choice.
# 2) Start an infinite loop using `while True` so the game can repeat for multiple rounds.
# 3) Take the user's choice as input and store it in `user_action`.
# (Expected inputs: "rock", "paper", or "scissors".)
# 4) Create a list `possible_actions` containing the three valid moves.
# 5) Use `random.choice(possible_actions)` to randomly select the computer’s move
# and store it in `computer_action`.
# 6) Display both choices (user and computer) using an f-string.
# 7) Compare `user_action` and `computer_action` to decide the result:
# a) If both are the same, print that it’s a tie.
# b) Else if the user chose "rock"
# i) If computer chose "scissors", user wins.
# ii) Otherwise, user loses (computer chose "paper").
# c) Else if the user chose "paper":
# i) If computer chose "rock", user wins.
# ii) Otherwise, user loses (computer chose "scissors").
# d) Else if the user chose "scissors":
# i) If computer chose "paper", user wins.
# ii) Otherwise, user loses (computer chose "rock").
# 8) After showing the result, ask the user if they want to play again
# and store the input in `play_again`.
# 9) If `play_again` is not "y", stop the game using `break`.
# Otherwise, the loop continues and a new round starts.
import random
while True:
    possible_actions= ["rock","paper","scissors"]
    user_action= input("Enter rock, paper, or scissors.")
    computer_action= random.choice(possible_actions)
    print(f"You picked {user_action}. The Computer picked {computer_action}.")
    if user_action==computer_action:
        print("Its a Tie.")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("You Win.")   
        else:
            print("You Lose")    
    elif user_action=="paper":    
        if computer_action=="rock":
            print("You Win.")   
        else:
            print("You Lose") 
    elif user_action=="scissors":    
        if computer_action=="paper":
            print("You Win.")   
        else:
            print("You Lose")  
    else:
        print("Invalid Choice! Please enter rock, paper, or scissors. ")
    play_again= input("Do You Want To Continue Playing? Enter Y for Yes or N for No.") 
    if play_again=='N':
        ("Thank You! for playing. See you Next Time.")


