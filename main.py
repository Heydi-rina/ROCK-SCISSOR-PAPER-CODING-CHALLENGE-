import random

#create a list of play option 
user_action = input ("Enter a choice Rock, Paper, Scissors):")
possible_actions = ["Rock", "Paper", "Scissors"]
computer_action = random.choice (possible_actions)
print (f"\nYou chose {user_action}, computer choose {computer_action}.\n")
if user_action == computer_action:

  print (f"\Both players selected {user_action}. It's a tie!")
elif user_action =="Rock":
  if computer_action == "Scissors":
   print ("Rock smashes scissors! You win!")
  else: 
   print ("Paper covers rock! You lose.")
elif user_action =="Paper":
  if computer_action =="Rock":
   print("Paper covers rock! You win!")
  else: 
    print ("Scissors cuts Paper! You lose.")
elif user_action =="scisssors":
  if computer_action =="paper": 
    print ("Scissors cuts paper! You win!")
  else: 
    print ("Rock smahes scissors! You lose.")

