# TODO
#from cs50 import get_int


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
    height = int(input("Enter height: "))
    
    if height <= 0 or height >= 9:
        return get_size()
    else:
        return height


def makeblock(num):
    block = "#"
    return block * num


def makespace(num):
    space = " "
    return space * num


main()
