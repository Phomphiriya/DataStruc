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

def encode(string,number):
    for i in range(string.size()):
        if string.head().islower():
            string.enQueue(chr((ord(string.deQueue())-ord('a') + number.head())%26 + ord('a')))
        elif string.head().isupper():
            string.enQueue(chr((ord(string.deQueue())-ord('A') + number.head())%26 + ord('A')))
        number.enQueue(number.deQueue())
    print(f'Encode message is :  {list(string.items)}')

string,number = input("Enter String and Code : ").split(',')
string = ''.join(string.split())
q1 = Queue(list(string))
q2 = Queue(list(map(int, number)))

encode(q1,q2)
print(f'Decode message is :  {list(string)}')



