#taking in the input demo
#check the file contest_input.txt to understand how this works

input_file = open("contest_input.txt")

def foo(this_line):
    item_list = this_line.split(", ")
    for item in item_list:
        #you'll want to do something more than just print, but you know... demo...
        print(item)

#loop through every line
for line in input_file:
    foo(line.strip() )  #strip removes the extra line break