#ACSL Scrabble
#Senior Contest 1 - 2013/2014

# set up special squares
DOUBLE_LETTER_SQUARES = list(range(3, 41, 6))
TRIPLE_LETTER_SQUARES = list()
DOUBLE_WORD_SQUARES = list()
TRIPLE_WORD_SQUARES = list()

for square in range(5, 41, 5):
	if square not in DOUBLE_LETTER_SQUARES:
		TRIPLE_LETTER_SQUARES.append(square)

for square in range(7, 41, 7):
	if square not in DOUBLE_LETTER_SQUARES and square not in TRIPLE_LETTER_SQUARES:
		DOUBLE_WORD_SQUARES.append(square)

for square in range(8, 41, 8):
	if square not in DOUBLE_LETTER_SQUARES and square not in TRIPLE_LETTER_SQUARES and square not in DOUBLE_WORD_SQUARES:
		TRIPLE_WORD_SQUARES.append(square)

def letter_value(letter):
	if letter == "A" or letter == "A":
		return 1
	elif letter == "D" or letter == "R":
		return 2
	elif letter == "B" or letter == "M":
		return 3
	elif letter == "V" or letter == "Y":
		return 4
	elif letter == "J" or letter == "X":
		return 8

def letter_in_location_value(letter, location):
	base_value = letter_value(letter)
	the_letter = base_value
	if location in DOUBLE_LETTER_SQUARES:
		the_letter = base_value * 2
	elif location in TRIPLE_LETTER_SQUARES:
		the_letter =  base_value * 3

	return the_letter

def word_score(word, start_location, direction):
	word_multiplier = 1
	word_value = 0

	if direction == "H":
		for index, square in enumerate(range(start_location, start_location+4)):
			if square in DOUBLE_WORD_SQUARES:
				word_multiplier *= 2
			elif square in TRIPLE_WORD_SQUARES:
				word_multiplier *= 3

			word_value += letter_in_location_value(word[index], square)

		return word_value * word_multiplier

	elif direction == "V":
		for index, square in enumerate(range(start_location, start_location+4)):
			current_square = start_location+10*index

			if current_square in DOUBLE_WORD_SQUARES:
				word_multiplier *= 2
			elif current_square in TRIPLE_WORD_SQUARES:
				word_multiplier *= 3

			word_value += letter_in_location_value(word[index], current_square)

		return word_value * word_multiplier

	else:
		return "Direction parsing error."


def process_problem(this_line, current_word):
    item_list = this_line.split(", ")
    best_score = 0
    
    for index, value in enumerate(item_list):
    	if index % 2 == 0:
    		this_score = word_score(current_word, int(value), item_list[index+1])
    		if this_score > best_score:
    			best_score = this_score

    return best_score
    
def set_word(this_line):
	item_list = this_line.split(", ")
	return "".join(item_list)

########################################################################################################

input_file = open("scrabble_test_input.txt")

# Loop through every line. Each line is one sample problem.
for line_number, line in enumerate(input_file):
	if line_number == 0:
		current_word = set_word(line.strip())
	else:
	    best_score = process_problem(line.strip(), current_word )  #strip removes the extra line break
	    print(best_score)


#used while testing
# print("DL: " , DOUBLE_LETTER_SQUARES)
# print("TL: ", TRIPLE_LETTER_SQUARES)
# print("DW: ", DOUBLE_WORD_SQUARES)
# print("TW: ", TRIPLE_WORD_SQUARES)

# print(word_score("JAVA", 1, "V"))
# print(word_score("JAVA", 2, "V"))
# print(word_score("JAVA", 3, "V"))