print("Welcome to Treasure Island.")
print(''' __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%% {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {} ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
 ejm97   /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /''')
print("Your mission is to find the treasure.")
direction = input("You're at a crossroad. Do you choose to go left or right?\n")
if direction == "left" or direction == "Left" or direction == "LEFT":
  lake = input("You have come to a lake. There is an island in the middle of the lake. The water is known to be home to \nvarious mysterious creatures, and there is not a single other soul in sight. Do you wait for a boat, or do you swim? ")
  if lake == "WAIT" or lake == "wait" or lake == "Wait":
    door = input("After an hour-long wait, you spot a fisherman's boat pass by, and finally arrive at the island unharmed. \nYou enter a house with 3 doors - a red, a blue and a yellow. Which one do you choose?")
    if door == "red" or door == "Red" or door == "RED":
      print("The door reveals a huge demon, hungry for your blood. Game over.")
    elif door == "blue" or door == "BLUE" or door == "Blue":
      print("The door reveals a ticking time bomb, its mechanism designed to be triggered by the opening of the door. \nGame over.")
    else:
      print("The door reveals the treasure you are looking for. You win!")
  else:
    print("You are attacked by a pack of lake sharks. Game over.")
else:
  print("The right road leads to a lion's den. You are surrounded on all sides. Game over.")
  