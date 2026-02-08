def numberofBits(n):
    ones = 0
    zeroes = 0

    while (n):

        if(n&1==1):
            ones += 1

        else:
            zeroes += 1

        n >>= 1

    print("\n\nNumber of ones: ", ones, "\nNumber of zeroes: ", zeroes)

number = int(input("Enter ur number: "))
numberofBits(number)