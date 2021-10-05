class Node:
    def __init__(self, data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None,None,None)
        self.tail = Node(None,None,self.head)
        self.head.next = self.tail

    def __str__(self):
        curr = self.head.next
        strt = ""
        while curr is not self.tail:
            strt += str(curr.data) + " "
            curr = curr.next

        if strt == "":
            return ""
        else:
            return "->".join(strt.split())

    def str_reverse(self):
        curr = self.tail.prev
        strt = ""
        while curr is not self.head:
            strt += str(curr.data) + " "
            curr = curr.prev

        if strt == "":
            return ""
        else:
            return "->".join(strt.split())

    def isEmpty(self):
        return self.head.next == self.tail

    def size(self):
        curr = self.head.next
        count = 0
        while curr != self.tail:
            count +=1
            curr = curr.next
        return count

    def append(self,data):
        new = Node(data,self.tail,self.tail.prev)
        self.tail.prev.next = new
        self.tail.prev = new

    def add_before(self, data):
        new = Node(data,self.head.next,self.head)
        self.head.next.prev = new
        self.head.next = new

    def insert(self,pos,data):
        if pos >= 0 and pos <= self.size():
            curr = self.head
            for i in range(pos):
                curr = curr.next
            new = Node(data,curr.next,curr)
            curr.next.prev = new
            curr.next = new
        else:
            print("Data cannot be added")

    def remove(self,data):
        try:
            curr = self.head.next
            pos = 0
            while curr.data != data:
                curr = curr.next
                pos += 1
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
            curr.next == None
            curr.prev == None
            print(f'removed : {data} from index : {pos}')
        except:
            print("Not Found!")

inp = input("Enter Input : ").split(',')
d = DoublyLinkedList()
for i in inp:
    i = i.split()
    case = i[0]
    if case == "A":
        d.append(i[1])
    elif case == "Ab":
        d.add_before(i[1])
    elif case == "I":
        temp = i[1].split(':')
        pos = temp[0]
        data = temp[1]
        d.insert(int(pos),data)
        if int(pos) >= 0 and int(pos) <= d.size():
            print(f'index = {pos} and data = {data}')
    elif case == "R":
        d.remove(i[1])
    print(f'linked list : {d}')
    print(f'reverse : {d.str_reverse()}')