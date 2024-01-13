# TODO
from cs50 import get_int


def main():
    size = get_size()
    countup = 1
    countdown = size - 1
    for i in range(size):
        print(makespace(countdown), end="")
        print(makeblock(countup), "", makeblock(countup))
        countup += 1
        countdown -= 1


def get_size():
    size = get_int("Height: ")
    if size <= 0 or size >= 9:
        return get_size()
    else:
        return size


def makeblock(num):
    block = "#"
    return block * num


def makespace(num):
    space = " "
    return space * num


main()
