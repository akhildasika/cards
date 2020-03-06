from CSM import Deck

deck1 = Deck()
deck1.create()
c = int(0)
d = int(0)

while(d == 0):
    b = int(input("1 to print: "))
    if(b == 1):
        deck1.shuffle()
        deck1.pt()
        b = 0
        a = int(input("2 to draw first card, 3 to reshuffle: "))
        if(a == 2):
            print(deck1.deal)
            a = 0
        else:
            a = 0
                
                


    




