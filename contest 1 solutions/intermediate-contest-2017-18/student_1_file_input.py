# ACSL Contest
# Intermediate
# Contest #1
#
#
# Author: WMCI Student (redacted)
# Date: December 9, 2017
#
#
#/////// Definitions //////////

def playCard(card, val):
    """ Takes a card value and total point value
        and checks for any special values before proceeding

        card and val must be int """
    if card == 10:
        card = -10
    elif card == 9:
        card = 0
    elif card == 14:
        if val + 14 > 99:
           card = 1
    return card

#/////// Files /////////////

fp = open('test_input.txt')# <---- Input File
sample = []
for line in fp:
    strippedLine = line.strip()
    doneLine = strippedLine.split(", ")
    sample.append(doneLine)
fp.close()

#/////// Program ///////////

case = []

for number, element in enumerate(sample):

    case = sample[number]# current case
    pointVal = int(case.pop(0))# initial point value

    for i, j in enumerate(case):# Replaces letters with the card's value
        if case[i] == 'T':
            case.insert(i, '10')
            case.remove('T')
        elif case[i] == 'J':
            case.insert(i, '11')
            case.remove('J')
        elif case[i] == 'Q':
            case.insert(i, '12')
            case.remove('Q')
        elif case[i] == 'K':
            case.insert(i, '13')
            case.remove('K')
        elif case[i] == 'A':
            case.insert(i, '14')
            case.remove('A')

    hand = []
    for i in range(3):# makes starting hand
        hand.append(int(case.pop(0)))

    while True:# The 'game' loop

        play = max(hand[0], hand[1], hand[2])# Plays the highest value card in the hand
        hand.remove(play)

        hand.append(int(case.pop(0)))# draws a card

        pointVal += playCard(play, pointVal)# adds the card value to the total
        if pointVal > 99:# checks to see if someone won yet
            Win = 'dealer'
            break

        dealer = int(case.pop(0))#dealer's play
        pointVal += playCard(dealer, pointVal)
        if pointVal > 99:# checks to see if someone won yet
            Win = 'player'
            break

    print(str(pointVal) + ", " + Win)# <--- Output