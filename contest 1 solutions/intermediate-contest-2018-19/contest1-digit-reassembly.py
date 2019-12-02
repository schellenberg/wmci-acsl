
def digit_reassembly(data):
    parts = data.split()

    the_number = parts[0]
    n = int(parts[1])

    total = 0
    for starting_number in range(len(the_number) - n+1):
        total += int(the_number[starting_number:starting_number+n])
        
    return total

input_file = open("contest1-sample-input.txt")
for line in input_file:
    try:
        print(digit_reassembly(line))
    except:
        print("Aww crap. I screwed up somewhere...")