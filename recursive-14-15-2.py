#recursive function - 2014/15 question 2

def f(x, y):
    if x > 10:
        return f(y-1, x-2) + 4
    elif x >= 5:
        return f(x+3, y-3) + 2
    else:
        return 3*x - 2*y

print( f(15, 12) )