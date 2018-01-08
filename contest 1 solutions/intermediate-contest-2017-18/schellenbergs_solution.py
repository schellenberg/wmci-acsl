#Ninety Nine Game
#Intermediate Contest 1 - 2017/2018

POINT_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 0, 'T': -10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def process_problem(this_line):
    global current_score, whose_turn

    item_list = this_line.split(", ")
    player_hand = list()

    for index, value in enumerate(item_list):
        if current_score <= 99:  #don't process anything after going above 99
        	if index == 0:
        		current_score = int(value)
        	elif index < 4:
        		player_hand.append(value)
        	elif index % 2 == 0:	#player's pickup
        		play_card(player_hand, value)
        	elif index % 2 == 1:
        		dealer_plays(value)

    return str(current_score), whose_turn


def choose_card_to_play(hand_list):
	SORT_ORDER = ('2','3','4','5','6','7','8','9','T','J','Q','K','A')
	which_card = 0

	for card in hand_list:
		order = SORT_ORDER.index(card)
		if order > which_card:
			which_card = order

	return SORT_ORDER[which_card]


def play_card(hand, new_card):
    global current_score, whose_turn

    card_to_play = choose_card_to_play(hand)
    value_of_card = POINT_VALUES[card_to_play]

    #make the ace count as a 1 instead of 14, if required
    if card_to_play == "A" and value_of_card + current_score > 99:  
        value_of_card = 1

    current_score += value_of_card

    #replace previous card with new pickup
    card_location = hand.index(card_to_play)
    hand[card_location] = new_card
    whose_turn = "dealer"

def dealer_plays(card):
    global current_score, whose_turn

    value_of_card = POINT_VALUES[card]

    #make the ace count as a 1 instead of 14, if required
    if card == "A" and value_of_card + current_score > 99:  
        value_of_card = 1

    current_score += value_of_card
    whose_turn = "player"

########################################################################################################

input_file = open("test_input.txt")

# Loop through every line. Each line is one sample problem.
for line in input_file:
    current_score = 0
    whose_turn = "player"

    final_score, winner = process_problem(line.strip())  #strip removes the extra line break
    print(str(final_score) + ", " + winner)
