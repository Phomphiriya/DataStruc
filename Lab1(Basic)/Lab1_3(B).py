def permu(inp):
    inp.reverse()
    ls1 = []
    ls1.append(inp)
    copyLis = inp.copy()
    
    if len(inp) == 3:
        for i in range(len(inp)-1):
            copyLis[i],copyLis[i+1]= copyLis[i+1],copyLis[i]
            newLis = copyLis.copy()
            ls1.append(newLis)
        copyLis[0],copyLis[-1] = copyLis[-1],copyLis[0]
        newLis = copyLis.copy()
        ls1.append(newLis)
        for i in range(len(inp)-1):
            copyLis[i],copyLis[i+1]= copyLis[i+1],copyLis[i]
            newLis = copyLis.copy()
            ls1.append(newLis)
            
    if len(inp) == 4:
        for i in range(len(inp)-1):
            copyLis[i],copyLis[i+1]= copyLis[i+1],copyLis[i]
            newLis = copyLis.copy()
            ls1.append(newLis)

        copyLis[0],copyLis[-1] = copyLis[-1],copyLis[0]
        newLis = copyLis.copy()
        ls1.append(newLis)
        
        for i in range(len(inp)-1):
            copyLis[i],copyLis[i+1]= copyLis[i+1],copyLis[i]
            newLis = copyLis.copy()
            ls1.append(newLis)

        for i in range(len(inp)-1):
            copyLis[i],copyLis[i+1]= copyLis[i+1],copyLis[i]
            newLis = copyLis.copy()
            ls1.append(newLis)
    return ls1


print("*** Fun with permute ***")
inp = list(map(int,input("input : ").split(',')))
print("Original Cofllection: ",inp)
print("Collection of distinct numbers:")
print("",permu(inp))