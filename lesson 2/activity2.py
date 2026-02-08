def SetorNotset(number, n):
    if number & (1 <<(n - 1)):
        print("\nSET")

    else:
        print("\nNOT SET")

number = int(input("Enter your number: "))
n = int(input("enter bit number: "))
SetorNotset(number, n)
