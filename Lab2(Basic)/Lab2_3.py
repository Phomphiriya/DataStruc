def Newrange(start=0,stop=0,step=1):
    ls1 = []
    i = start
    while i < stop:
        i2 = float(i)
        ls1.append(round(i2,3))
        i += step
    return tuple(ls1)


print("*** New Range ***")
inp = list(map(float,input("Enter Input : ").split()))
if len(inp) == 3:
    print(Newrange(inp[0],inp[1],inp[2]))
elif len(inp) == 2:
    print(Newrange(inp[0],inp[1]))
elif len(inp) == 1:
    print(Newrange(stop=inp[0]))

# *** New Range ***
# Enter Input : 10
# (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)

# *** New Range ***
# Enter Input : 3.2 6.32
# (3.2, 4.2, 5.2, 6.2)

# *** New Range ***
# Enter Input : 0.112 6.45 1.35
# (0.112, 1.462, 2.812, 4.162, 5.512)

# *** New Range ***
# Enter Input : 1 7 1.2
# (1.0, 2.2, 3.4, 4.6, 5.8)