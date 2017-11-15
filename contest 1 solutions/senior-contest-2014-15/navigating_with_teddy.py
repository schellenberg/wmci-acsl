def process_problem(this_line):
    #turn the line into a list
    item_list = this_line.split(", ")
    print(item_list)

    first_starting_city = item_list[0]
    second_starting_city = item_list[1]
    

input_file = open("contest_test_input.txt")

for line in input_file:
    process_problem( line.strip() )  #strip gets rid of the extra line break