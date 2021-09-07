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
q1 = Queue()
q2 = Queue()
activity = {"0":"Eat","1":"Game","2":"Learn","3":"Movie"}
location = {"0":"Res.","1":"ClassR.","2":"SuperM.","3":"Home"}
lover = 0
check1 = 0
check2 = 0
for i in inp:
    i = i.split()
    q1.enQueue(i[0])
    q2.enQueue(i[1])
q1c = ', '.join(q1.items)
q2c = ', '.join(q2.items)
print(f'My   Queue = {q1c}')
print(f'Your Queue = {q2c} ')
print(f'My   Activity:Location = ',end='')
for i in q1.items:
    myac = i[0]
    yourac = i[-1]
    check1 += 1
    if check1 < q1.size():
        print(f'{activity[myac]}:{location[yourac]}',end=', ')
    else:
        print(f'{activity[myac]}:{location[yourac]}',end='')
print(end='\n')
print(f'Your Activity:Location = ',end='')
for i in q2.items:
    myac = i[0]
    yourac = i[-1]
    check2 += 1
    if check2 < q2.size():
        print(f"{activity[myac]}:{location[yourac]}",end=', ')
    else:
        print(f'{activity[myac]}:{location[yourac]}',end='')
print(end='\n')
for i in range(q1.size()):
    if q1.items[0][0] == q2.items[0][0] and q1.items[0][-1] == q2.items[0][-1]:
        lover += 4
        q1.deQueue()
        q2.deQueue()
    elif q1.items[0][0] != q2.items[0][0] and q1.items[0][-1] == q2.items[0][-1]:
        lover += 2
        q1.deQueue()
        q2.deQueue()
    elif q1.items[0][0] == q2.items[0][0] and q1.items[0][-1] != q2.items[0][-1]:
        lover += 1
        q1.deQueue()
        q2.deQueue()
    else: 
        lover -= 5
        q1.deQueue()
        q2.deQueue()
if lover >= 7:
    print(f"Yes! You're my love! : Score is {lover}.")
elif lover > 0:
    print(f"Umm.. It's complicated relationship! : Score is {lover}.")
else:
    print(f"No! We're just friends. : Score is {lover}.")


# Enter Input : 0:0 2:0,1:3 3:3,2:1 2:1
# My   Queue = 0:0, 1:3, 2:1
# Your Queue = 2:0, 3:3, 2:1 
# My   Activity:Location = Eat:Res., Game:Home, Learn:ClassR.
# Your Activity:Location = Learn:Res., Movie:Home, Learn:ClassR.
# Yes! You're my love! : Score is 8.

# Enter Input : 2:1 2:1
# My   Queue = 2:1
# Your Queue = 2:1 
# My   Activity:Location = Learn:ClassR.
# Your Activity:Location = Learn:ClassR.
# Umm.. It's complicated relationship! : Score is 4.

# Enter Input : 0:1 2:3,3:2 3:2
# My   Queue = 0:1, 3:2
# Your Queue = 2:3, 3:2 
# My   Activity:Location = Eat:ClassR., Movie:SuperM.
# Your Activity:Location = Learn:Home, Movie:SuperM.
# No! We're just friends. : Score is -1.