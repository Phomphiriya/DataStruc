def findMin(number):
    if len(number) <= 1:
        return number
    findMin()

inp = list(map(int,input("input : ").split()))
print(findMin(inp))