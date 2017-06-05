"""  Ball.py
Author: Adjoa Darien
Last Modified: December 14, 2012
Description: Represents a moving ball in a graphics window

Python 2.x
"""

from time import sleep
from random import randrange, random
from graphics import *

class Ball:
    
    
    def __init__(self, win):
      
      center = Point(100, 100)
      self.circ = Circle(center, 30)
      self.circ.setFill("red")
      self.circ.draw(win)
      
      self.dx = randrange(2,5)
      self.dy = randrange(2,5)

      self.count = 0
      
        
    def getCenter(self):
      return self.circ.getCenter()
        
    def getRadius(self):
      return self.circ.getRadius()

    def reverseX(self):
            self.dx = self.dx*(-1)
            return self.dx

    def reverseY(self):
        self.dy = self.dy*(-1)
        return self.dy

    def move(self, win):
        centerPt = self.getCenter()
        xCoord = centerPt.getX()
        yCoord = centerPt.getY()

        #if the ball gets to the edge of the screen, reverse the direction of the ball    
        if (xCoord-30)<=0 or (xCoord+30) >= 300:
            self.dx = self.reverseX()
            self.count +=1
            
            
        if (yCoord-30)<=0 or (yCoord+30) >= 300:
            self.dy = self.reverseY()
            self.count +=1
            

        self.circ.move(self.dx, self.dy)

        sleep(0.01)

        if self.count%100 == 0:
            self.goFaster()
            self.count +=1
        

    def goFaster(self):
        self.dx = self.dx *(1+random())
        self.dy = self.dy *(1+random())

    def front(self):
        #returns coordinates of the edge of the ball
        centerPt = self.getCenter()
        xCoord = centerPt.getX()
        yCoord = centerPt.getY()
        self.frontX = xCoord+30
        self.frontY = yCoord
        self.frontCoord = Point(self.frontX, self.frontY)
        return self.frontCoord


		
""" Main Driver function to test Ball class """ 		
def main():
  w = 300
  h = 300
  pWin = GraphWin("Pong", w, h )
  
  #create an instance of the Ball class
  b = Ball(pWin)
  print "centre x value for ball:", b.getCenter().getX()
  print "center y value for ball:", b.getCenter().getY()
  print
  print "front x value for ball:", b.front().getX()
  print
  print "After ball moves..."

  while pWin.checkMouse() == None:
      b.move(pWin)
      
  print "centre x value for ball:", b.getCenter().getX()
  print "center y value for ball:", b.getCenter().getY()
  print
  print "front x value for ball:", b.front().getX()
  print
      
  pWin.getMouse()
  pWin.close()
  
  
""" Only runs main if asked to run Ball.py"""
if __name__ == '__main__':
    main()
    
