class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        current, string = self.head, str(self.head.data) + " "
        while current.next != None:
            string += str(current.next.data) + " "
            current = current.next
        return string

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = p

    def addHead(self, item):
        p = Node(item)
        p.next = self.head
        self.head = p

    def search(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return "Found"
            else:
                current = current.next
        return "Not Found"

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            index += 1
            current = current.next
        return -1

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count +=1
            current = current.next
        return count

    def pop(self, pos = None):
        if self.isEmpty():
            return "Out of Range"
        elif pos <= self.size():
            p = self.head
            if pos == None:
                while p.next.next != None:
                    p = p.next
                p.next = None
            elif pos == 0:
                self.head = self.head.next
                return "Success"
            else:
                count = 0
                while count != pos-1:
                    p = p.next
                    count += 1
                p.next = p.next.next
                return "Success"
        else:
            return "Out of Range"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1}".format(L.search(i[3:]), i[3:]),end='')
        print(" in",L)
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)