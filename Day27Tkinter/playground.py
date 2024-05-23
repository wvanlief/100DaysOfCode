def add(*args):
    # a = 0
    # for n in args:
    #     a += n
    # return a
    return sum(args) #args is a tuple so it is iterable

print(add(3, 5, 1, 5))