from PlayingCard import*
from random import*



class Deck():
    def __init__(self): #create a new deck with 4 suits and 13 ranks
        self.cardList = []
        for s in ['d', 'c', 'h', 's']:
            for r in range(1,14):
                self.cardList.append(PlayingCard(r,s))
       
                
    def shuffle(self): #Shuffle the card everytime
        shuffle(self.cardList)
        return self.cardList

    def dealCard(self): #Every time user takes out a card, remove it from the cardlist so there is so repetition
        index = randrange(0,len(self.cardList))
        return self.cardList.pop(index)
    def cardLeft(self): 
        
        return len(self.cardList)

def main():
    deck = Deck()
    deck.shuffle()
    print(deck.dealCard())
    print(deck.cardLeft())



if __name__ == "__main__":
    main()
    

        
