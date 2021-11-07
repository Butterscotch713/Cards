
import random
import time
from main import game

def rules(x,cardslist):
    if(x=='Yes'):
        print("Your goal is to be the first to reach the number 31. You will be given 3 cards to start with.\n"
          "Only cards of the same suite may have their values added together \n"
          "Face cards have a value of 10, and Aces have a value of 11 \n"
          "If you hit 31, the computer will detect your victory \n"
          "If you do not have 31, you may draw a random card from the deck, or pick up the card your opponent discarded \n"
          "If you have close to 31 or believe you have higher than the computer, you may knock \n"
          "When someone knocks, the other player gets one more turn, and then whoever had the highest value wins \n"
          "To knock type 'knock' \n"
          "To select a new card you may type either 'pile' to take your opponents rejected card or 'deck' to draw a new card from the deck \n"
          "However you must then drop a card by typing 'drop 'cardname' before you may end your turn\n"
          "The card names and values are as follows: \n",
          cardslist)
    elif(x=="No"):
        return
    elif((x!="Yes")):
        print("error, please type that again: ")
        x=input()
        rules(x)

def initialcards():
    cardlist={"Queen of Hearts":10,"King of Hearts":10,"Jack of Hearts":10,"Ace of Hearts":11,
              "Two of Hearts":2,"Three of Hearts":3,"Four of Hearts":4, "Five of Hearts":5,
              "Six of Hearts":6, "Seven of Hearts":7, "Eight of Hearts":8,
              "Nine of Hearts":9, "Ten of Hearts":10,
              "Queen of Spades": 10, "King of Spades": 10, "Jack of Spades": 10, "Ace of Spades": 11,
              "Two of Spades": 2, "Three of Spades": 3,
              "Four of Spades": 4, "Five of Spades": 5, "Six of Spades": 6, "Seven of Spades": 7, "Eight of Spades": 8,
              "Nine of Spades": 9, "Ten of Spades": 10,
              "Queen of Clubs": 10, "King of Clubs": 10, "Jack of Clubs": 10, "Ace of Clubs": 11,
              "Two of Clubs": 2, "Three of Clubs": 3,
              "Four of Clubs": 4, "Five of Clubs": 5, "Six of Clubs": 6, "Seven of Clubs": 7, "Eight of Clubs": 8,
              "Nine of Clubs": 9, "Ten of Clubs": 10,
              "Queen of Diamonds": 10, "King of Diamonds": 10, "Jack of Diamonds": 10, "Ace of Diamonds": 11,
              "Two of Diamonds": 2, "Three of Diamonds": 3,
              "Four of Diamonds": 4, "Five of Diamonds": 5, "Six of Diamonds": 6, "Seven of Diamonds": 7, "Eight of Diamonds": 8,
              "Nine of Diamonds": 9, "Ten of Diamonds": 10}
    lst=list()
    for key in cardlist.keys():
        lst.append(key)

    playcards=random.sample(lst,3)
    lst.remove(playcards[0])
    lst.remove(playcards[1])
    lst.remove(playcards[2])
    compcards=random.sample(lst,3)
    lst.remove(compcards[0])
    lst.remove(compcards[1])
    lst.remove(compcards[2])
    playcardsval=cardlist[playcards[0]],cardlist[playcards[1]],cardlist[playcards[2]]
    compcardsval = cardlist[compcards[0]], cardlist[compcards[1]], cardlist[compcards[2]]

    return (playcards,playcardsval,compcards,compcardsval,lst,cardlist)

def addheartsval(cards,cardslist):
    acc=0
    for card in cards:
        if("Hearts" in card):
            acc=acc+cardslist[card]
    return acc
def addspadessval(cards,cardslist):
    acc=0
    for card in cards:
        if("Spades" in card):
            acc=acc+cardslist[card]
    return acc

def addclubssval(cards,cardslist):
    acc=0
    for card in cards:
        if("Clubs" in card):
            acc=acc+cardslist[card]
    return acc

def adddiamondsval(cards,cardslist):
    acc=0
    for card in cards:
        if("Diamonds" in card):
            acc=acc+cardslist[card]
    return acc

def checkplayerwin(heart,club,spade,diamond):
    if ((heart == 31) or (club == 31) or (spade == 31) or (diamond == 31)):
        print("You Win!")
        return True
    else:
        return False


def checkcompwin(heart,club,spade,diamond,compcards):
    if ((heart == 31) or (club == 31) or (spade == 31) or (diamond == 31)):
        print("The computer won :( It had the cards: ",compcards )
        return True
    else:
        return False


def dropc(dropcard,playercards):
    playercards.remove(dropcard)




def pileadd(cardontop,cardtodiscard,playercards):
    playercards.append(cardontop)
    dropc(cardtodiscard,playercards)

def do(action):
    if((action!="pile") and (action!="deck") and (action!="knock")):
        print("Please enter a valid action")
        action=input()
        do(action)
    else:
        return


def playeradd(cardontop, drop, playcards):
    pileadd(cardontop, drop, playcards)


def deckplayeradd(dro,playercards):
        dropc(dro,playercards)

def runrules(x, cardslist):
    if(x=="Yes"):
        rules(x, cardslist)
    elif(x=="No"):
        return
    else:
        print("Please enter Yes or No")
        x=input()
        runrules(x,cardslist)

def computerdecide(cardontop,compcards,hearts,spades,clubs,diamonds,cardslist):
    cardtoremove = random.choice(compcards)
    cardtoadd=cardontop
    if("Hearts" in compcards[0] or "Hearts" in compcards[1] or "Hearts" in compcards[2]):
        if(hearts>=spades and hearts>=clubs and hearts>=diamonds):
                if("Hearts" in cardontop):
                    cardtoadd=cardontop

                    if ("Hearts" in cardtoremove):
                        cardtoremove = random.choice(compcards)

                else:
                    cardtoadd = random.choice(cardslist)
                    if ("Hearts" in cardtoremove):
                        cardtoremove = random.choice(compcards)


    elif ("Spades" in compcards[0] or "Spades" in compcards[1] or "Spades" in compcards[2]):
        if (spades >= hearts or spades >= clubs or spades >= diamonds ):
                    if ("Spades" in cardontop):
                        cardtoadd=cardontop
                        if ("Spades" in cardtoremove):
                            cardtoremove = random.choice(compcards)

                    else:
                        cardtoadd = random.choice(cardslist)
                        if ("Spades" in cardtoremove):
                            cardtoremove = random.choice(compcards)


    elif("Clubs" in compcards[0] or "Clubs" in compcards[1] or "Clubs" in compcards[2]):
        if(clubs>=spades or clubs>=hearts or clubs>=diamonds):
                    if("Clubs" in cardontop):
                        cardtoadd=cardontop
                        if ("Clubs" in cardtoremove):
                            cardtoremove = random.choice(compcards)

                    else:
                        cardtoadd=random.choice(cardslist)
                        if ("Clubs" in cardtoremove):
                            cardtoremove = random.choice(compcards)

    elif ("Diamonds" in compcards[0] or "Diamonds" in compcards[1] or "Diamonds" in compcards[2]):
        if (diamonds >= spades or diamonds >= clubs or diamonds >= hearts):
                    if ("Diamonds" in cardontop):
                        cardtoadd=cardontop
                        compcards.append(cardontop)
                        if ("Diamonds" in cardtoremove):
                            cardtoremove=random.choice(compcards)
                    else:
                        cardtoadd = random.choice(cardslist)
                        if ("Diamonds" in cardtoremove):
                            cardtoremove = random.choice(compcards)

    else:
        cardtoadd=random.choice(cardslist)
        compcards.append(cardtoadd)

    compcards.append(cardtoadd)
    compcards.remove(cardtoremove)
    cardontop=cardtoremove
    ret=list()
    ret.append(compcards)
    ret.append(cardontop)
    return(ret)

def playerknocked(cardontop,compcards,lst,cardslist,playheart,playclub,playspade,playdiamond,compheart,compclub,compspade,compdiamond):
    compturn = computerdecide(cardontop, compcards, compheart, compspade, compclub, compdiamond, lst)
    compcards = compturn[0]
    compheart = addheartsval(compcards, cardslist)
    compclub = addclubssval(compcards, cardslist)
    compspade = addspadessval(compcards, cardslist)
    compdiamond = adddiamondsval(compcards, cardslist)
    compsvals=[(compheart),(compclub),(compspade),(compdiamond)]
    compmax=max(compsvals)
    playervals=[(playheart),playclub,playspade,playdiamond]
    playermax=max(playervals)
    checkcompwin(compheart, compclub, compspade, compdiamond, compcards)
    if(compmax>playermax):
        print("The computer won :(")
    elif(playermax>compmax):
        print("You won!")
    else:
        print("You tied, but because you're human, you win!")
    return True




def playCards():
    initcar = initialcards()
    shufflepile = list()
    cardslist = initcar[5]
    print("Welcome to 31! In this game you will always go before the computer unless there is a winner on the dealt cards")
    print("Do you need to see the rules? Type 'Yes' or 'No'")
    x = input()
    runrules(x,cardslist)
    print("The game will automatically begin in 30 seconds")
    time.sleep(30)
    # rules(x,cardslist)
    print("You will always have the first move")
    playcards = initcar[0]
    print("Your cards are: ")
    print(", ".join(playcards))
    playcardsval = initcar[1]
    compcards = initcar[2]
    compardsval = initcar[3]
    lst = initcar[4]
    cardontop=random.choice(lst)
    lst.remove(cardontop)
    shufflepile.append(cardontop)
    playheart = addheartsval(playcards, cardslist)
    playclub = addclubssval(playcards, cardslist)
    playdiamond = adddiamondsval(playcards, cardslist)
    playspade = addspadessval(playcards, cardslist)
    compheart=addheartsval(compcards,cardslist)
    compclub=addclubssval(compcards,cardslist)
    compspade=addspadessval(compcards,cardslist)
    compdiamond=adddiamondsval(compcards,cardslist)
    print("Your current heart value: ", playheart)
    print("Your current spade value: ", playspade)
    print("Your current club value: ", playclub)
    print("Your current diamond value: ", playdiamond)
    checkplayerwin(playheart,playclub,playspade,playdiamond)
    checkcompwin(compheart,compclub,compspade,compdiamond,compcards)
    print("The current card on top of the pile is: ",cardontop, "\nWould you like to take that card or a random card from the deck?")
    dopls=input()
    do(dopls)
    # cardinhand(dro,playcards)
    while(playheart!=31 and playclub!=31 and playspade!=31 and playdiamond!=31 and compdiamond!=31 and compheart!=31 and compspade!=31 and compclub!=31):
        if(dopls=="pile"):
            print("What card would you like to drop? ")
            dro = input()
            playeradd(cardontop,dro,playcards)
            cardontop=dro
            shufflepile.append(cardontop)
            if(cardontop in lst):
                lst.remove(cardontop)
            else:
                for card in playcards :
                    if(card in lst):
                        lst.remove(card)

            # print("The new card on top is: ",cardontop)
        elif(dopls=="knock"):
            win=playerknocked(cardontop,compcards,lst,cardslist,playheart,playclub,playspade,playdiamond,compheart,compclub,compspade,compdiamond)
            if(win==True):
                break
        else:
        # elif(dopls=="deck"):
            newcard = random.choice(lst)
            print("You picked up: ", newcard)
            print("What card would you like to drop? ")
            dro = input()
            playcards.append(newcard)
            deckplayeradd(dro,playcards)
            cardontop=str(dro)
            shufflepile.append(cardontop)
            if (cardontop in lst):
                lst.remove(cardontop)
            else:
                for card in playcards:
                    if (card in lst):
                        lst.remove(card)

        print("Your new cards are: ")
        print(", ".join(playcards))
        playspade = addspadessval(playcards, cardslist)
        playclub = addclubssval(playcards, cardslist)
        playdiamond = adddiamondsval(playcards, cardslist)
        playheart = addheartsval(playcards, cardslist)
        print("Your current heart value: ", playheart)
        print("Your current spade value: ", playspade)
        print("Your current club value: ", playclub)
        print("Your current diamond value: ", playdiamond)
        print("The new card on top is : ", cardontop) #bug w/ card on top when initial card to drop is not in deck
        win=checkplayerwin(playheart,playclub,playspade,playdiamond)
        if(win==True):
            break

        print("The computer is currently taking it's turn")

        compturn=computerdecide(cardontop,compcards,compheart,compspade,compclub,compdiamond,lst)
        compcards=compturn[0]
        cardontop=compturn[1]
        compheart = addheartsval(compcards, cardslist)
        compclub = addclubssval(compcards, cardslist)
        compspade = addspadessval(compcards, cardslist)
        compdiamond = adddiamondsval(compcards, cardslist)
        win=checkcompwin(compheart,compclub,compspade,compdiamond,compcards)
        if (win == True):
            break
        print("The current card on top is: ",cardontop)
        print("Your cards are: ",playcards)
        print("Would you like to draw from the deck or pile?")
        if(len(lst)==0):
            lst=shufflepile
            shufflepile=list()
        dopls=input()
    return







if(game=="Thirty One"):
    playCards()


