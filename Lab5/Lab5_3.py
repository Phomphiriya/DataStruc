class Node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(data):
    if data == None:
        list = []
    else:
        list = data
    # print(list)
    head = Node(list[0])
    curr = head
    for i in data[1:]:
        newNode = Node(i)
        curr.next = newNode
        curr = curr.next
    return head

def printList(head):
    curr = head
    while curr != None:
        print(curr,end=' ')
        curr = curr.next
    print()

def mergeOrderesList(L1,L2):
    curr1 = L1
    curr2 = L2
    
    mergeHead = Node(None,None)
    mergeCurr = mergeHead
    while curr1 is not None and curr2 is not None:
        if curr1.data <= curr2.data:
            mergeCurr.next = curr1
            curr1 = curr1.next
        else:
            mergeCurr.next = curr2
            curr2 = curr2.next
        mergeCurr = mergeCurr.next
    
    while curr1 is not None:
        mergeCurr.next = curr1
        curr1 = curr1.next
        mergeCurr = mergeCurr.next
    
    while curr2 is not None:
        mergeCurr.next = curr2
        curr2 = curr2.next
        mergeCurr = mergeCurr.next
    
    mergeHead = mergeHead.next
    return mergeHead

#################### FIX comand ####################   

inp = input("Enter 2 Lists : ").split('/')
LL1 = createList(list(map(int,inp[0].split(','))))
LL2 = createList(list(map(int,inp[1].split(','))))
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)