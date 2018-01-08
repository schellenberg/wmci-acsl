#---------------------------------------------------
# ACSL Intermediate Division 2017-2018
# WMCI Student (redacted)
# Dec 09, 2017
#---------------------------------------------------

# note that you need to enter the input WITH NO SPACES

import re
# define the functions
def alpha():
    for i in list:
        if i.isalpha():
            return True

def check():
    if alpha() == True:
        for i in range (0,list.count('T')):
            number = input_list.index('T')
            input_list[number] = '10'
    if alpha() == True:
        for i in range (0,list.count('A')):
            number = input_list.index('A')
            input_list[number] = '14'
    if alpha() == True:
        for i in range (0,list.count('J')):
            number = input_list.index('J')
            input_list[number] = '11'
    if alpha() == True:
        for i in range (0,list.count('Q')):
            number = input_list.index('Q')
            input_list[number] = '12'
    if alpha() == True:
        for i in range (0,list.count('K')):
            number = input_list.index('K')
            input_list[number] = '13'


#set
point = 0
player = 1
dealer = 1
new_value = 0
time_through = 1
list = input("input: ")
input_list = re.split('[,]', list) 

check()
input_list = [int(i) for i in input_list]

point = input_list[0]
card_1 = input_list[1]
card_2 = input_list[2]
card_3 = input_list[3]

for i in range(4,12,2):
# player
    if point <= 99:
        player = player +1
        three_card_list = [card_1, card_2, card_3]
        new_value = input_list[i]
        if card_1 == max(three_card_list):
            larger_value = card_1
            card_1 = new_value
        elif card_2 == max(three_card_list):
            larger_value = card_2
            card_2 = new_value
        elif card_3 == max(three_card_list):
            larger_value = card_3
            card_3 = new_value
         
        if larger_value == 9:
            point = point + 0
        elif larger_value == 10:
            point = point - 10
        elif larger_value == 14:
            if point + 14 > 99:
                point = point + 1
            else:
                point = point + 14
        else:
            point = point + larger_value

#dealer
    if point <= 99:
        dealer = dealer + 1
        if time_through == 1:
            if input_list[5] == 9:
                point = point + 0
            elif input_list[5] == 10:
                point = point - 10
            elif input_list[5] == 14:
                if point + 14 > 99:
                    point = point + 1
                else:
                    point = point + 14
            else:
                point = point + input_list[5]
            time_through = time_through +1
        
        elif time_through == 2:
            if input_list[7] == 9:
                point = point + 0
            elif input_list[7] == 10:
                point = point - 10
            elif input_list[7] == 14:
                if point + 14 > 99:
                    point = point + 1
                else:
                    point = point + 14
            else:
                point = point + input_list[7]
            time_through = time_through +1
        
        elif time_through == 3:
            if input_list[9] == 9:
                point = point + 0
            elif input_list[9] == 10:
                point = point - 10
            elif input_list[9] == 14:
                if point + 14 > 99:
                    point = point + 1
                else:
                    point = point + 14
            else:
                point = point + input_list[9]
            time_through = time_through +1

#output
if player > dealer:
    print("output:",point, "dealer")
else:
    print("output:",point, "player")

    