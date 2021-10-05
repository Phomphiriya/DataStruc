inp = int(input('Enter Input : '))
k = inp+1
k2 = inp+1
for l in range(1,inp+3):
    print("."*k,end='')
    print("#"*l,end='')
    if l == 1 or l == inp+2:
        print("+"*(inp+2),end='')
    else:
        print("+" + "#"*inp + "+",end='')
    k -= 1
    print(end='\n')
for l in range(1,inp+3):
    if l == 1 or l == inp+2:
        print("#"*(inp+2),end='')
    else:
        print("#" + "+"*inp + "#",end='')
    print("+"*(k2+1),end='')
    print("."*(l-1),end='')
    k2 -= 1
    print(end='\n')

# Enter Input : 1
# ..#+++
# .##+#+
# ###+++
# ###+++
# #+#++.
# ###+..

# Enter Input : 2
# ...#++++
# ..##+##+
# .###+##+
# ####++++
# ####++++
# #++#+++.
# #++#++..
# ####+...