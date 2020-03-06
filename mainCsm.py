from CSM import Deck
from cardcountClass import Card
decks = Deck()
x = int(input("how many decks: "))
for i in range(x):
    deck1 = Deck()
    deck1.create()
    for i in range(4):
            for j in range(0,14):
                    decks.cards.append(Card(i, j))
c = int(0)
d = int(0)

while(d == 0):
    b = int(input("1 to print: "))
    if(b == 1):
        decks.shuffle()
        decks.pt()
        b = 0
        a = int(input("2 to draw first card, 3 to reshuffle: "))
        if(a == 2):
            print(decks.deal)
            a = 0
        else:
            a = 0
                
                


    




