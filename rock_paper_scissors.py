starter = input ("Welcome to this game of rock-paper-scissors. Do you wish to play? Yes or No.").lower()
if starter == "yes":
  user = input ("Yay! Get ready to lose. What do you choose - rock, paper or scissors? ").lower()
  print("1, 2 , 3... shoot!")
  print("You chose " + user)

  options = ["rock", "paper", "scissors"]
  import random
  comp = str((random.choice(options)))
  print("I chose " + comp)

  if user == comp:
    print("We have reached a tie. I am insulted.")
  elif user == "rock" and comp == "scissors" or user == "scissors" and comp == "paper" or user == "paper" and comp == "rock":
    print ("You win. Cheater.")
  elif user == "rock" and comp == "paper" or user == "paper" and comp == "scissors" or user == "scissors" and comp == "rock":
    print ("I win. Loser.")
  else:
    print ("The value you entered was not appropriate. Therefore, I win. Hee hee.")
else:
  print ("No problem! Come back later.")
  
