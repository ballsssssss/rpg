import pygame, sys
from pygame.locals import QUIT
import os

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
  
  
def foodhunting():
  os.system("clear")
  print ("\nYou walk around and you find a big snake monster thing which you start attacking for food to get for the Spider.")

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
      print ("\nwell too bad now the spider killed you noob")
      quit()
while True:
  launchgame = input ("\033[1;32mDo you wanna launch the RPG The Epic?")
  
  if launchgame == 'yes':
    gamestart()
    break
  if launchgame == 'no':
    print ("try again")