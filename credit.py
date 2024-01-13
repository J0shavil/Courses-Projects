# TODO
import string
import sys


def main():
    AMEX = False
    MC = False
    VISA = False
    creditnum = 0

    creditnum = str(getinput())

    """
    print(creditnum)
    """

    numcount = count_digits(creditnum)

    if numcount < 13:
        print("INVALID")

    digits_list = [int(char) for char in creditnum]

    if digits_list[0] == 5 and digits_list[1] < 6 and digits_list[1] > 0:
        MC = True
    if digits_list[0] == 4:
        VISA = True
    if digits_list[0] == 3 and digits_list[1] == 4 or digits_list[1] == 7:
        AMEX = True

    """
    print(digits_list)
    """

    ValidCardCheck = check_credit_num(creditnum, numcount, digits_list)

    if ValidCardCheck == False:
        print("INVALID")
        sys.exit(1)

    if MC == True and ValidCardCheck == True:
        print("MASTERCARD")
    if VISA == True and ValidCardCheck == True:
        print("VISA")
    if AMEX == True and ValidCardCheck == True:
        print("AMEX")
    else:
        print("INVALID")
        sys.exit(1)


def count_digits(num):
    return len(num)


def check_credit_num(creditnum, numcount, digits_list):
    count = 0
    count2 = 0
    i = 0
    n = 0
    list = []
    list2 = []

    if float((numcount / 2) % 2) == 0:
        while i != numcount / 2:
            list.append(str(digits_list[n] * 2))
            n += 2
            i += 1
        list = "".join(list)
        i = 0
        while i < len(list):
            count += int(list[i])
            i += 1

        i = 0
        n = 1
        while i < numcount / 2:
            list2.append(str(digits_list[n]))
            n += 2
            i += 1
        list2 = "".join(list2)
        i = 0
        while i < len(list2):
            count2 += int(list2[i])
            i += 1

    if float((numcount / 2) % 2) > 0:
        n = 1
        if numcount > 13:
            while i < (numcount / 2) - 1:
                list.append(str(digits_list[n] * 2))
                i += 1
                n += 2

            list = "".join(list)
            i = 0
            while i < len(list):
                count += int(list[i])
                i += 1

        if numcount == 13:
            n = 1
            i = 0
            while i < (numcount / 2) - 1:
                list.append(str(digits_list[n] * 2))
                i += 1
                n += 2
            list = "".join(list)
            i = 0
            while i < len(list):
                count += int(list[i])
                i += 1

            i = 0
            n = 0
            while i < (numcount / 2):
                list2.append(str(digits_list[n]))
                n += 2
                i += 1
            list2 = "".join(list2)
            i = 0
            while i < len(list2):
                count2 += int(list2[i])
                i += 1

        if numcount > 13:
            n = 0
            i = 0
            while i < (numcount / 2):
                list2.append(str(digits_list[n]))
                i += 1
                n += 2

            list2 = "".join(list2)
            i = 0
            while i < len(list2):
                count2 += int(list2[i])
                i += 1

    if (count + count2) % 10 == 0:
        return True
    else:
        return False


def getinput():
    number = input("Number: ")
    try:
        number = int(number)
        if number > 13:
            return number
    except ValueError:
        return getinput()


main()
