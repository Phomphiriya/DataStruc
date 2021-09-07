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

inp = input("Enter String and Code : ").split(',')
q = Queue()
ascii = []
ans = []
for i in inp[0]:
    if i != " ":
        q.enQueue(i)
        ascii.append(ord(i))
print(ascii)
for i in ascii:
    ans += chr(i+int(inp[1]))

print(f'Eecode message is :  {ans}')
print(f'Decode message is :  {q.items}')