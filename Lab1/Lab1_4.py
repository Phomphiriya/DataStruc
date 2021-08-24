print("*** Fun with Drawing ***")
num = int(input("Enter input : "))

for i in range(2*num-2):   
    for j in range(i):       
        if j % 2 == 0:
            print("#",end='')   
        else:
            print(".",end='')

    for j in range((4*num-3)-(2*i)):
        if i % 2 == 0:
            print("#",end='')
        else:
            print(".",end='')

    for j in range(i-1,-1,-1):
        if(j%2==0):
            print('#',end='')
        else:
            print('.',end='')
    print(" ")

for i in range(2*num-2,-1,-1):   
    for j in range(i):       
        if j % 2 == 0:
            print("#",end='')   
        else:
            print(".",end='')

    for j in range((4*num-3)-(2*i)):
        if i % 2 == 0:
            print("#",end='')
        else:
            print(".",end='')

    for j in range(i-1,-1,-1):
        if(j%2==0):
            print('#',end='')
        else:
            print('.',end='')

    print(" ")
