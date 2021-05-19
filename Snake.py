# This is a comment
# Snake Tutorial

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox 

class cube(object):
    rows = 0
    w = 0
    def __init__(self,start,dirnx=1,dirny=0,color=(220, 189, 255)):
      pass

    def move(self, dirnx, dirny):
      pass

    def draw(self, surface, eyes=False):
      pass

class snake(object):
  body = []
  turns = {} #kinda like a dictionary or set
  def __init__(self, color, pos):
    self.color = color
    self.head = cube(pos) # Head of the snake or starting position of the snake
    self.body.append(self.head) #Appending the body of the snake to the head
    self.dirnx = 0 # Direction snake is moving
    self.dirny = 1

    def move(self):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()

        keys = pygame.key.get_pressed()
        
        for key in keys: 
          if keys[pygame.K_LEFT]:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] # adding current position of the head of the snake and is set to which direction we turned, 
            
          elif keys[pygame.K_RIGHT]:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
          
          elif keys[pygame.K_UP]:
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

          elif keys[pygame.K_DOWN]:
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] # The [:] is an arrow?

        for i, c in enumerate(self.body): #looking through list of pos we have. i stands for index and c stands for cube
          p = c.pos[:]
          if p in self.turns:
            turn = self.turns[p]
            c.move(turn[0], turn[1]) 
            if i == len(self.body)-1:
              self.turns.pop(p)
          else: 
            if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1]) # checks whether or not we are moving off the screen. This is when you are for example making your snake run into the right wall it will continue and come back through the left side of the screen and move across the screen.
            elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
            elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
            elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)
            else: c.move(c.dirnx,c.dirny) 


    def reset(self, pos):
      pass

    def addCube(self):
      pass

    def draw(self, surface):
      for i, c in enumerate(self.body):
        if i == 0:
          c.draw(surface, True)
        else:
          c.draw(surface)

def drawGrid(w, rows, surface):
  sizeBetween = w // rows # width integer divided by rows, since we are figuring out the size between the lines being drawn to form the cubes. makes sure there is no No large decimal numbers

  x = 0
  y = 0
  for l in range(rows):
    x = x + sizeBetween
    y = y + sizeBetween

    pygame.draw.line(surface, (255,255,255), (x,0), (x,w)) # this draws 2 lines for every loop of this for loop. The (x,0), (x,w) are the start position and the end positions of the line. This line is vertical
    pygame.draw.line(surface, (255,255,255), (0,y), (w,y)) # This line is horizontal


def redrawWindow(surface):
  global rows, width
  surface.fill((0,0,0))
  drawGrid(width, rows, surface)
  pygame.display.update()

def randomSnack(rows, items):
  pass

def message_box(subject, content):
  pass

def main():
  global width, rows, s, snack
  width = 500
  rows = 20 # if you have like 10 here instead the game will not last as long because there will not be as much room for the snake to go. The number must go in 500 evenly. How many rows or columns you are going to have. If you want it to be harder you can set it to 10.
  s = snake((189, 255, 198), (10,10)) # creates the snakes color and position, in this case the snake is starting in the center
  win = pygame.display.set_mode((width, width)) # win will create a surface and you don't need a height because they are gonna be 500x500/same size
  flag = True

  clock = pygame.time.Clock()

  while flag:
    pygame.time.delay(50) # delays 50 miliseconds every time so program doesn't run so fast. The lower this goes the fast it's gonna be
    clock.tick(10) # make sure our game doesn't run more than 10 frames per second. If this is too low it will make it slower
    redrawWindow(win)


  pass




main()

# 2 main objects; the snake object and the cube object. The snake object is going to contain the cube object. 