def processLine(this_line):
    list_of_items = this_line.split(", ")
    print(list_of_items)


the_file = open("the-input.txt")

for line in the_file:
    processLine(line.strip())