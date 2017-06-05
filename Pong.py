"""  Pong.py
Author: Adjoa Darien
Last Modified: December 14, 2012
Description: A simple one-player version of the game Pong.

Python 2.x
"""

from Ball import Ball
from Paddle import Paddle

from time import sleep
from random import randrange, random
from graphics import *

class Pong:
        def __init__(self):

            self.win = GraphWin("Pong", 300, 300)
            self.ball = Ball(self.win)
            self.paddle = Paddle(self.win, 50, Point(290,150))
            self.fixedX = 280

            self.ballMid = self.ball.getCenter()
            self.ballMidX = self.ballMid.getX()
            self.ballMidY = self.ballMid.getY()

            self.instructions = "Click space to either side of the paddle"
            instructions = Text(Point(150,20), self.instructions)
            self.instruct = instructions

            self.hits = 0
            self.level = 0
            self.printtowin = "Hits:", self.hits, "Level:", self.level
            printscore = Text(Point(150,20), self.printtowin)
            self.score = printscore

            self.printtowin2 = "Game Over"
            printendgame = Text(Point(150,35),self.printtowin2)
            self.endgame = printendgame

        def checkContact(self):
                #track the coordinates of the ball's center
                self.ballMid = self.ball.getCenter()
                #if the ball is within the range of the x line that marks the front of the paddle then
                if (self.ball.front().getX())>= self.fixedX:
                        #if the ball is between the top and bottom ends of the paddle
                        if (self.ball.front().getY())>= self.paddle.pad.getP2().getY() and (self.ball.front().getY())<= self.paddle.pad.getP1().getY():
                                return True
                
                    
        def gameOver(self):
                self.ballMid = self.ball.getCenter()
                #if the ball passes the x line where the paddle might be then the game ends
                if (self.ballMid.getX()+15)>= self.fixedX:
                        return True
                else:
                        return False
                
 
        def play(self):
                #display the instructions
                self.instruct.draw(self.win)
                sleep(1)
                self.instruct.undraw()
                sleep(1)
                #display the score and level of the game
                self.score.draw(self.win)
                while (self.gameOver() == False):
                        savePt = self.win.checkMouse()
                        if savePt != None:
                            self.paddle.move(self.win, savePt)

                        self.ball.move(self.win)

                        #if the ball hits the paddle
                        if self.checkContact()== True:
                            #reverse the direction of the ball
                            self.ball.reverseX() 
                            self.hits +=1
                            self.level = self.level

                            #update the score
                            self.score.undraw()
                            self.printtowin = "Hits:", self.hits, "Level:", self.level
                            printscore = Text(Point(150,20), self.printtowin)
                            self.score = printscore
                            self.score.draw(self.win)

                            #if the number of hits is evenly divisible by 5
                            if self.hits%5 ==0:
                                    #update the level
                                    self.level +=1
                                    self.score.undraw()
                                    self.printtowin = "Hits:", self.hits, "Level:", self.level
                                    printscore = Text(Point(150,20), self.printtowin)
                                    self.score = printscore
                                    self.score.draw(self.win)
                                    #increase the speep of the ball
                                    self.ball.goFaster()
                        sleep(0.1)
                
                if (self.gameOver() == True):
                        #print game over message
                        self.endgame.draw(self.win)
                        self.win.getMouse()
                        self.win.close()
                                    
                
def main():
        p = Pong()

        p.play()
        
        print "Game Over"
        print "Number of hits:", p.hits
        print "Level:", p.level
    
main()
    
        
        
