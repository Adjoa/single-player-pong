"""  Paddle.py
Author: Adjoa Darien
Last Modified: December 14, 2012
Description: Represents a moving paddle in a graphics window

Python 2.x
"""

from time import sleep
from random import randrange, random
from graphics import *

class Paddle:

    def __init__(self, win, length, middle):

        #middle of paddle
        self.mid = middle
        self.midx = middle.getX()
        self.midy = middle.getY()

        #length of paddle
        self.len = length
        
        #mark all the points in the rectangle that makes up the paddle
        self.pt1 = Point(self.midx, self.midy -(self.len/2))
        self.pt2 = Point(self.midx, self.midy +(self.len/2))
        self.pt3 = Point(self.midx+10, self.midy -(self.len/2))
        self.pt4 = Point(self.midx+10, self.midy +(self.len/2))

        #front of paddle
        self.front = Line(self.pt1, self.pt2)

        #the paddle
        self.pad = Rectangle(self.pt2, self.pt3)

        self.pad.draw(win)

    def move(self,win, click):
        control = click
        controlY = control.getY()

        #if the user clicks above the paddle then move in that direction
        if controlY > self.pt1.getY():
            self.midy = self.midy +10
            self.pad.move(0, +10)
        #if the user clicks below the paddle then move in that direction
        elif controlY < self.pt2.getY():
            self.midy = self.midy -10
            self.pad.move(0, -10)

       
        
    
""" Main Driver function to test Paddle class """     
def main():
  w = 300
  h = 300
  pWin = GraphWin("Pong", w, h )
  
  #create an instance of the Paddle class
  paddle = Paddle(pWin, 50, Point(290, 150))

  print "Length: ", paddle.len
  print
  print "Paddle's Midpoint:", paddle.mid
  print "Paddle's x value at midpoint:", paddle.midx
  print "Paddle's y value at midpoint:", paddle.midy
  print
  print "After paddle moves..."

  for i in range(1):
      paddle.move(pWin, pWin.getMouse())
      
  print "Paddle's x value at midpoint:", paddle.midx
  print "Paddle's y value at midpoint:", paddle.midy
    
          
  pWin.getMouse()
  pWin.close()
  
  
""" Only runs main if asked to run Ball.py"""
if __name__ == '__main__':
    main()
    

    
    
    
