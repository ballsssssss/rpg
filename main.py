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
print(1)
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
  print ("hi")

def gamestart():
  os.system("clear")
  incave = int(input ("The game launches and you spawn in a cave with a bunch of ores and shiny gems, Do you wish to stand up? (1 for yes and 2 for no)"))
  if incave == 1:
    print ("As soon as you stood up you saw a gaint spider looking down on you and it wants to talk you")
    print ("The spider says You need to bring me food now or you die, take this sword now go")

    sword = int(input ("Do you pickup the sword or no?(1 for yes and 2 for no)"))
    if sword == 1:
      foodhunting()
    if sword == 2:
      print ("well too bad now the spider killed you noob")
      quit()
while True:
  launchgame = input ("\033[1;32mDo you wanna launch the RPG The Epic?")
  
  if launchgame == 'yes':
    gamestart()
    break
  if launchgame == 'no':
    print ("try again")
  if launchgame == 'ah':
    test()
  
  