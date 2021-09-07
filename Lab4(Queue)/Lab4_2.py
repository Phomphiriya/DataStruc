class Queue:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def head(self):
        return self.items[0]
    def deQueue(self):
        return self.items.pop(0)
    def enQueue(self,i):
        return self.items.append(i)
    def __str__(self):
        return str(self.items)
    def insertQueue(self,index,i):
        self.items.insert(index,i)

inp = input("Enter Input : ").split(',')
q = Queue()
o = 0
for i in inp:
    i = i.split()
    
    if i[0] == 'EN':
        q.enQueue(i[1])
    elif i[0] == 'ES':
        q.insertQueue(o,i[1])
        o += 1
    else:
        try:
            print(q.head())
            q.deQueue()
            if o > 0:
                o -= 1
        except:
            print("Empty")

# Enter Input : EN 1,EN 2,D,D,D,EN 3,D
# 1
# 2
# Empty
# 3

# Enter Input : EN 1,ES 2,D,D,D,EN 3,D
# 2
# 1
# Empty
# 3

# Enter Input : EN 1,ES 2,ES 99,D,D,D,EN 3,D
# 2
# 99
# 1
# 3