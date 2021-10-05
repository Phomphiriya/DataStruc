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

inp = input("Enter Input : ").split(',')
q = Queue()

for i in inp:
    i = i.split()
    if i[0] == 'E':
        q.enQueue(i[1])
        print(q.size())
    else:
        try:
            print(q.deQueue(),"0")
        except:
            print("-1")
if q.isEmpty():
    print("Empty")

print(' '.join(q.items))

# Enter Input : E 10,E 20,E 30,E 40,D,D
# 1
# 2
# 3
# 4
# 10 0
# 20 0
# 30 40

# Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
# 1
# 2
# 3
# 4
# 10 0
# 4
# 5
# 20 0
# 30 0
# 40 0
# 50 0
# 60 0
# -1
# Empty
