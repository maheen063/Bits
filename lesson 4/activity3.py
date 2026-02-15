def computePower(x, y):
    result = 1

    while (y > 0):
        if (y % 2 == 0):
            x = x * x
            y = y // 2

        else:
            result = result * x
            y = y - 1
    
    return result

x = int(input("Enter the x value: "))
y = int(input("Enter the y value: "))
print("Total: ", computePower(x, y))