def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

inp = list(map(int,input("Enter Input : ").split()))
if inp[0] < 0 and inp[1] < 0:
    x = inp[1]
    y = inp[0]
elif inp[0] > inp[1]:
    x = inp[0]
    y = inp[1]
else:
    x = inp[1]
    y = inp[0]
if x == 0 and y == 0 :
    print("Error! must be not all zero.")
else:
    print (f'The gcd of {x} and {y} is : ',end="")
    print (gcd(int(abs(x)),int(abs(y))))