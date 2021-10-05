def weirdSub(x,y):
    x,y = int(x),int(y)
    strX = str(x)
    while x > 0 and y > 0:
        if strX[-1] == "0":
            x /= 10
            y -= 1
            strX = str(int(x))
        else:
            if int(strX[-1]) > y:
                x -= y
                return int(x)
            intX = int(strX[-1])
            y -= intX
            x -= intX
            strX = str(int(x))
    return int(x)


inp = input("Enter num and sub : ").split()
print(weirdSub(inp[0],inp[1]))


# Enter num and sub : 163 8
# 12

# Enter num and sub : 10 1
# 1

# Enter num and sub : 2021 5
# 20

# Enter num and sub : 2077 55
# 0