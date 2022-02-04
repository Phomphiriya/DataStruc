def Median(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        j = i - 1
        while j>=0 and curr < arr[j]:
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = curr
    mid = int(len(arr)/2)
    if len(arr) % 2 == 0 : return (arr[mid-1]+arr[mid])/2
    else : return arr[mid]/1

l = [int(e) for e in input("Enter Input : ").split()]
inp1=[]
inp2=[]
for i in range(len(l)):
    inp1.append(l[i])
    inp2.append(l[i])
    print("list = {} : median = {}".format(inp2,Median(inp1)))