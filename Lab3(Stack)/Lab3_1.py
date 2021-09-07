class Stack:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    
    def __str__(self):
        return str(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def push(self,i):
        self.items.append(i)
    
    def pop(self):
        self.items.pop()
    
    def peek(self):
        return self.items[-1]

inp = input("Enter Input : ").split(',')
s = Stack()
for i in inp:
    a = i.split()
    if a[0] == "A":
        s.push(a[1])
        print("Add = {} and Size = {}".format(a[1],s.size()))
    else:
        if s.size() > 0:
            print("Pop = {}".format(s.peek()),end=' ')
            s.pop()
            print("and Index = {}".format(s.size()))
        else:
            print("-1")
if s.size() > 0:
    print("Value in Stack =",' '.join(s.items))
else:
    print("Value in Stack = Empty")

# Enter Input : A 10,A 20,A 30,A 40,P,P
# Add = 10 and Size = 1
# Add = 20 and Size = 2
# Add = 30 and Size = 3
# Add = 40 and Size = 4
# Pop = 40 and Index = 3
# Pop = 30 and Index = 2
# Value in Stack = 10 20

# Enter Input : A 10,A 20,A 30,A 40,P,A 50,A 60,P,P,P,P,P,P
# Add = 10 and Size = 1
# Add = 20 and Size = 2
# Add = 30 and Size = 3
# Add = 40 and Size = 4
# Pop = 40 and Index = 3
# Add = 50 and Size = 4
# Add = 60 and Size = 5
# Pop = 60 and Index = 4
# Pop = 50 and Index = 3
# Pop = 30 and Index = 2
# Pop = 20 and Index = 1
# Pop = 10 and Index = 0
# -1
# Value in Stack = Empty

# Enter Input : P,A 99,P,P,A 88,P,P,A 12,A 13,A 86
# -1
# Add = 99 and Size = 1
# Pop = 99 and Index = 0
# -1
# Add = 88 and Size = 1
# Pop = 88 and Index = 0
# -1
# Add = 12 and Size = 1
# Add = 13 and Size = 2
# Add = 86 and Size = 3
# Value in Stack = 12 13 86
