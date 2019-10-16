import random 
import sys

print ("Rock, paper, scissors, shoot!")
player1 = input('Player 1 - Enter your choice: ')   # prompts user input of rock, paper or scissors

rando = random.randint (0,2)                        # chooses rock, paper, or scissors by random
options = ['rock', 'paper', 'scissors']
winner = ""
player2 = options[rando]              
print("Player 2 chose:", player2)

# Check for a tie
if  (player1 == player2):    
    print("Tie!!")
    sys.exit()

# Check for winner
elif (player1 == "rock" and player2 != "scissors") or (player1 == "paper" and player2 != "rock") or (player1 == "scissors" and player2 != "paper"):   
    winner = "Player 2"
else: winner = "You"

print(winner, "won!!")



   
