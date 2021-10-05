class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(l=[]):
    arr = []
    for i in range(len(l)):
        arr.append(Node(l[i]))
    for i in range(len(arr)):
        try: arr[i].next = arr[i+1]
        except: arr[i].next = None
    return arr[0]

def scarmble(head, b, r, size):
    indexB =  int(b/100*size)
    indexR =  int(r/100*size)
    print(f'Start : {printLL(head)}')
    (format(321,".2f"))
    head1 = bottomUp(head , indexB)
    print(f'BottomUp {format(b, ".3f")} % : {printLL(head1)}')

    head2 = riffle(head1 , indexR)
    print(f'Riffle {format(r, ".3f")} % : {printLL(head2)}')

    head3 = deRiffle(head2 , indexR , size )
    print(f'Deriffle {format(r, ".3f")} % : {printLL(head3)}')

    head4 = bottomUp(head3 , size - indexB)
    print(f'Debottomup {format(b, ".3f")} % : {printLL(head4)}')
    return head4

def deRiffle(head , indexR , size):
    newHead = Node(None)
    cur = newHead
    newHead2 = Node(None)
    cur2 = newHead2
    i = 0
    if indexR <= int(size / 2):
        while head:
            if i < indexR * 2:
                if i % 2 == 0:
                    cur.next = head
                    cur = cur.next
                if i % 2 == 1:
                    cur2.next = head
                    cur2 = cur2.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
            i+=1
        cur.next = newHead2.next
        cur2.next = None
    else:
        index = size - indexR
        while head:
            if i < index * 2:
                if i % 2 == 1:
                    cur.next = head
                    cur = cur.next
                if i % 2 == 0:
                    cur2.next = head
                    cur2 = cur2.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
            i+=1
        cur2.next = newHead.next
        cur.next = None
    return newHead.next if indexR <= int(size / 2) else newHead2.next    

def riffle(head , indexR):
    newHead1 = head
    newHead2 = head
    curHead = Node(None)
    cur = curHead
    for i in range(indexR):
        if i == indexR-1:
            temp = newHead2.next
            newHead2.next = None
            newHead2 = temp
        else: newHead2 = newHead2.next
    
    def newCur(cur , newH):
        cur.next = newH
        cur = cur.next
        newH = newH.next
        return cur , newH

    while newHead2 or newHead1:
        if newHead1 and newHead2:
            cur , newHead1 = newCur(cur , newHead1)
            cur , newHead2 = newCur(cur , newHead2)
        else:
            if newHead1:  cur , newHead1 = newCur(cur , newHead1)
            elif newHead2: cur , newHead2 = newCur(cur , newHead2)

    curHead = curHead.next
    return curHead

def bottomUp(head , indexB):
    oldHead = head
    for i in range(indexB):
        head = head.next
    newHead = head
    while head.next: 
        head = head.next
    head.next = oldHead
    for i in range(indexB - 1):
        oldHead = oldHead.next
    oldHead.next = None
    return newHead

def printLL(h):
    s = ''
    while h:
        s+= h.value+' '
        h = h.next
    return s

def SIZE(h):
    i = 0
    while h:
        i+=1
        h = h.next
    return i

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        h = scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        h = scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)