def findSum(inp):
    ans = []
    check5 = []
    if len(inp) < 3:
        return "Array Input Length Must More Than 2"
    else:
        for i in range(len(inp)):
            for j in range(i+1,(len(inp))):
                for k in range(j+1,(len(inp))):
                    eqFive = inp[i] + inp[j] + inp[k]
                    ls = [inp[i] , inp[j] , inp[k]]
                    if eqFive == 5 and ls not in ans:
                        check5.append(ls)
        
        for m in check5:
            m.sort()
            if m in ans:
                pass
            else:
                ans.append(m)
        return ans

inp = list(map(int,input("Enter Your List : ").split()))
print(findSum(inp))

# Enter Your List : -25 -10 -7 -3 2 4 8 10
# [[-7, 2, 10], [-7, 4, 8]]

# Enter Your List : -3 2 4 6 8 10
# [[-3, 2, 6]]

# Enter Your List : -100 100
# Array Input Length Must More Than 2

# Enter Your List : 5 -5 5 -5 5 -5 5 5 -5 -5 -5 -5 5
# [[-5, 5, 5]]