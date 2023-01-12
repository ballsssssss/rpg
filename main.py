import pygame, sys
from pygame.locals import QUIT
import os
from tabulate import tabulate 
# activate the pygame library .
pygame.init()
X = 1000
Y = 600
# create the display surface object
# of specific dimension..e(X, Y).
display = pygame.display.set_mode((X, Y))
# set the pygame window name
pygame.display.set_caption('image') 
# create a surface object, image is drawn on it.
imp = pygame.image.load("MarioNSMBUDeluxe.png").convert()
# Using blit to copy content from one surface to other
display.blit(imp, (0, 0))
# paint screen one time
pygame.display.flip()
status = True


def test():
  # create the display surface object
  # of specific dimension..e(X, Y).
  display = pygame.display.set_mode((X, Y))
  # create a surface object, image is drawn on it.
  spider = pygame.image.load("spider 2.jpg").convert()
  # Using blit to copy content from one surface to other
  display.blit(spider, (-150, 0))
  # paint screen one time
  pygame.display.flip()
  global status
  status = True

def encountersystem():
  int(input ("What do you choose to do? (1 to Challenge, in progress 2 to Run, in progress 3 to Check inventory)"))
  while True:
      import random
      player = input ("Type either rock, paper or scissors.")
      possible_actions = ["rock", "paper", "scissors"]
      snakeaction = random.choice(possible_actions)
      print(f"\nYou chose {player}, Snake chose {snakeaction}.\n")
      
      if player == snakeaction:
          print(f"Both of you selected {player}. It's a tie and so both you and the snake die from a mysterious force!")
          print ("Try again")
      elif player == "rock":
          if snakeaction == "scissors":
              print("Rock smashes scissors! You win and and so the Snake tears off some flesh and gives it to you!")
              break
          else:
              print("Paper covers rock! You lose so the Snake hits you with some deadly venom and you die.")
              print ("Try again")
      elif player == "paper":
            if snakeaction == "rock":
              print("Paper covers rock! You win and and so the Snake tears off some flesh and gives it to you!")
              break
            else:
              print("Scissors cuts paper! You lose and so the Snake hits you with some deadly venom and you die.")
              print ("Try again")
      elif player == "scissors":
          if snakeaction == "paper":
              print("Scissors cuts paper! You win and so the Snake tears off some flesh and gives it to you!")
              break
          else:
              print("Rock smashes scissors! You lose so the Snake hits you with some deadly venom and you die.")
              print ("Try again")
  print ("To be continued")        
  
def foodhunting():
  os.system("clear")
  print ("\nYou walk around and you find a big snake monster thing which starts challenging you to a game of Rock, Paper and Scissors.")
  encountersystem()
  
def gamestart():
  test()
  os.system("clear")
  incave = int(input ("\nThe game launches and you spawn in a cave with a bunch of gold and shiny gems, Do you wish to stand up? (1 for yes and 2 for no)"))
  if incave == 1:
    print ("\nAs soon as you stood up, you saw a gaint spider looking down on you and it wants to talk you")
    print ("\nThe spider says You need to bring me food now or you die, take this sword now go")

    sword = int(input ("\nDo you pickup the sword or no?(1 for yes and 2 for no)"))
    if sword == 1:
      print ("\nNew Item Obtained: Sword which does 2-5 DMG")
      foodhunting()
    if sword == 2:
      print ("\nwell too bad now the Spider killed you noob")
      quit()
while True:
  launchgame = input ("\033[1;32mDo you wanna launch the RPG The Epic?")
  
  if launchgame == 'yes':
    gamestart()
    break
  if launchgame == 'no':
    print ("try again")