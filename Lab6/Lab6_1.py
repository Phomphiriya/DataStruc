def findMinimum(number):
    if len(number) == 1:
        return number[0]
    else:
        minNumber = findMinimum(number[1:])
        min = number[0]
        if minNumber < min:
            min = minNumber
        return min
inp = list(map(int,input("Enter Input : ").split()))
print(f'Min : {findMinimum(inp)}')