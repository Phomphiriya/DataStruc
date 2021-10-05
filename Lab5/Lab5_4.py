class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class Linkedlist:
    def __init__(self):
        self.head = Node(None,None)
        self.size = 0

    def __str__(self):
        curr = self.head.next
        strt = ""
        count = 0
        while curr != None:
            strt += str(curr.data) + " "
            curr = curr.next
            if count >= self.size:
                return "Found Loop"
            count += 1
        if strt == "":
            return "Empty"
        else:
            return "->".join(strt.split())
    
    def isEmpty(self):
        return self.head.next == None
    
    def append(self, data):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(data, None)
        self.size += 1
    
    def set_next(self,sender,receiver):
        curr_sender = self.head
        for i in range(sender+1):
            curr_sender = curr_sender.next
        curr_receiver = self.head
        for i in range(receiver+1):
            curr_receiver = curr_receiver.next
        print(f'Set node.next complete!, index:value = {sender}:{curr_sender.data} -> {receiver}:{curr_receiver.data}')
        curr_sender.next = curr_receiver

L = Linkedlist()
# print(L.size)
# print(L.isEmpty())
inp = input("Enter input : ").split(',')

for i in inp:
    j = i.split()
    case = j[0]
    if case == 'A':
        L.append(j[1])
        print(L)
    elif case == 'S':
        k = j[1].split(':')
        sender = int(k[0])
        receiver = int(k[1])
        if L.isEmpty():
            print("Error! {list is empty}")
        else:
            # print(L.size)
            if sender >= L.size or sender < 0:
                print("Error! {index not in length}:",sender)
            elif receiver >= L.size or receiver < 0:
                L.append(receiver)
                print("index not in length, append :",receiver)
            else:
                # print(sender,receiver)
                L.set_next(sender,receiver)
if str(L) != "Found Loop":
    print("No Loop")
print(L)