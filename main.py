import random

def winner():
  print("Congratulations, you win!")
  play_again()

def play_again():
  replay = input("Play again? ('Y' or 'N') ")
  if replay == "Y": the_game()

def random_end_game():
  gameOver = [
    "Game over, you got kicked by a donkey.", 
    "Your penis shriveled up. You Die. Game Over."]
  print(random.choice(gameOver))
  play_again()

def three_door_game():
  q3 = input("You've come to 3 doors.  One is red, one yellow, and one blue.  Which door do you choose? type 'red', 'yellow', or 'blue'. ").lower()
  if q3 == 'yellow':
    winner()
  elif q3 == 'red':
    print("Red meant fire, you burned alive.")
    play_again()
  elif q3 == 'blue':
    print("Blue meant water, you opened the door and the ocean came in and drowned you.")
    play_again()
  else:
    print("Game over dummy.  You can't spell red, blue, or yellow.")
    play_again()

def the_game():
  print('''
  *******************************************************************************
            |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/_____ /
  *******************************************************************************
  ''')
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.") 

  #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

  #Write your code below this line 👇
  q1 = input("Would you like to go left or right to start? type 'left' or 'right'. ").lower()
  if q1 == 'left': 
    q2 = input("You've come across a river, would you like to smim across or wait for the boat? type 'swim' or 'wait'. ").lower()
    if q2 == 'wait':
      three_door_game()
    else:
      random_end_game()
  else:
    random_end_game()

the_game()