def BoubleSort(sequence):
    for i in range(len(sequence)-1):
        swaped = False

        for j in range(len(sequence)-1-i):
            if sequence[j] > sequence[j+1]:
                swaped = True
                sequence[j],sequence[j+1] = sequence[j+1],sequence[j]
                
        if not swaped :
            break
    return sequence
    
inp = list(map(int,input("Enter Input : ").split()))
ans = BoubleSort(inp)
print(ans)