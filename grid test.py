from graphics import *
from time import*
from random import*
from Memory import*



def main():
    win = GraphWin("word cloud", 800, 800)
    memory = Memory()
    
    win.setBackground("lightsteelblue1")
    ptList = []



##    for x in range (50,800,80): #Use the length of the longest word to find out the suitable space
##            for y in range (50,800,100): #The height doesn't matter much because the letters are given in a certain range.
##                ptList.append(Point(x,y))  #Append new points to the list
##   
##    for point in ptList:
##        point.draw(win)

##    .
            


    "This is the learning phase - the player is given a set of cards to remember"
    for i in range (1):
        memory.learning(win,300,400)
        sleep(1)
        memory.undraw()

    "This is the testing phase"
    memory.testing(win, 120, 750, 300 ,500,90 , 100)
    
    
    #memory.renewWin()
    
    
main()
            
