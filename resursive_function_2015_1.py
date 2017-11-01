def f(x):
    if x >= 10:
        return 2*f(x-3)-4
    elif x >= 8:
        return f(x+1) + f(x-2)
    elif x >= 5:
        return f(x-4) - 1
    else:
        return x+3

