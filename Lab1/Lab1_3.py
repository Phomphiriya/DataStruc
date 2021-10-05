def permute(inp):
    ls1 = []
    inp.reverse()
    ls1.append(inp.copy())
    for round in range(1, len(inp) - 1):
        copyls = inp.copy()

        for i in range(len(inp) - 1):
            if i != 0 :
                copyls[i], copyls[i + 1] = copyls[i + 1], copyls[i]
                ls1.append(copyls.copy())
                
            newls = copyls.copy()
            for i in range(len(newls) - 1):
                newls[i], newls[i + 1] = newls[i + 1], newls[i]
                ls1.append(newls.copy())
                
        if round < len(inp) - 2:
            inp[round + 1], inp[round + 2] = inp[round + 2], inp[round + 1]
            ls1.append(inp.copy())

    return ls1

print('*** Fun with permute ***')

inp = list(map(int,input("input : ").split(',')))

print('Original Cofllection: ', inp)
print('Collection of distinct numbers:')
print('', permute(inp))

# *** Fun with permute ***
# input : 1,2,3
# Original Cofllection:  [1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]

#  *** Fun with permute ***
# input : 1,1,2,3
# Original Cofllection:  [1, 1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], 
#  [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], 
#  [1, 1, 3, 2], [1, 1, 2, 3], [3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], 
#  [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], 
#  [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3]]