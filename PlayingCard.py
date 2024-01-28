
from random import *



class PlayingCard: #Create a class to call each card
    def __init__ (self,rank,suit):
        self.rank = rank
        self.suit = suit

    def getRank(self): #Return rank of the card
        return self.rank 

    def getSuit(self): #Return suit of the card
        return self.suit
    
    def value (self):
        if self.rank > 10: #For special letter cards
            self.value = 10
        else:
            self.value = rank
            
    def __str__ (self): #This mod names the cards
        name = '' 
        if self.rank == 1:
            name = 'Ace'
        elif self.rank == 11:
            name = 'Jack'
        elif self.rank == 12:
            name = 'Queen'
        elif self.rank == 13:
            name = 'King'
        else:
            name = self.rank
    
        return ('{0} of {1}'.format(name,self.suit))




   
        

if __name__ == "__main__":
    main()
