from os import P_PGID
import random

User_wins = 0
compputer_wins = 0

optioin = ["rock", "paper", "scissors"]

while True:

    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in optioin:
        continue
    random_number = random.randint(0, 2)    
    # rock: 0 ,paper: 1 ,scissors: 2
    computer_pick = optioin[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("you  won")
        User_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        User_wins += 1

    elif user_input == "scissors" and computer_pick  == "paper":
        print('you won')
        User_wins += 1

    else:
         print("you lost")
         compputer_wins += 1  

print("yo won " , User_wins, "times")
print("the computer won " , compputer_wins , "times")
print("goodbye!")