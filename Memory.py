from Deck import*
from PlayingCard import*
from graphics import*


class Memory:
      
    def __init__(self, dHand=[]):
            #constructor that initializes instance variables
            #it also gives the playingDeck an initial shuffle
        self.dHand = dHand
    
        self.deck = Deck()
        self.deck.shuffle()
        self.images = []  #To undraw the cards when the game is done
        
    def learning(self,win,xpos,ypos):
            
        #player cards
        for i in range (4):
            self.dHand.append(self.deck.dealCard())


        for card in self.dHand:
            cardRank = card.getRank()
            cardSuit = card.getSuit()
            file = "playingcards/" + cardSuit + str(cardRank) + ".gif"
            pImage = Image(Point(xpos, ypos) , file)
            pImage.draw(win)
            self.images.append(pImage)
            xpos = xpos + 100
##            
##            for card in range (4):
            
##            for card in range (5,8):
##                xpos = xpos + 100
##                ypos = ypos + 30

    def undraw(self):
        for card in self.images:
            card.undraw()

    def testing(self,win, xstart, xend, ystart, yend, xjump , yjump):
        ptList = []
        for x in range (xstart,xend, xjump): #Use the length of the longest word to find out the suitable space
                for y in range (ystart,yend, yjump): #The height doesn't matter much because the letters are given in a certain range.
                    ptList.append(Point(x,y))  #Append new points to the list
   
        for point in ptList:
            point.draw(win)

        for i in range (10):
            self.dHand.append(self.deck.dealCard())
            
        
        for card in self.dHand:
            index = randrange(0,len(ptList))
            pt = ptList[index]
            
            cardRank = card.getRank()
            cardSuit = card.getSuit()
            file = "playingcards/" + cardSuit + str(cardRank) + ".gif"
            pImage = Image(Point(pt.getX(),pt.getY()) , file)
            pImage.draw(win)
            self.images.append(pImage)
            ptList.pop(index)
            
            

            
    def hit(self, win, xPos, yPos):
        
            #adds a new card to the player's hand and places it at xPos, yPos
        playerCard = self.deck.dealCard()
        self.pHand.append(playerCard)
        cardRank = playerCard.getRank()
        cardSuit = playerCard.getSuit()
        file = "playingcards/" + cardSuit + str(cardRank) + ".gif"
        pImage = Image(Point(xPos, yPos) , file)
        pImage.draw(win)
        self.images.append(pImage)
    
        
            
       
    def dealerFlip(self, win, xPos, yPos): #When the player hits stand, the first card of  dealer is flipped
        cardRank = self.dHand[0].getRank()
        cardSuit = self.dHand[0].getSuit()
        file = "playingcards/" + cardSuit + str(cardRank) + ".gif"
        dImage = Image(Point(xPos , yPos) , file)
        dImage.draw(win)
        self.images.append(dImage)
        

    def renewWin(self):
        for card in self.images:
            card.undraw()

        #Restart everything again
        self.images = []
        self.pHand = []
        self.dHand = []
        self.deck = Deck()
        self.deck.shuffle()

        
























        
        
    
