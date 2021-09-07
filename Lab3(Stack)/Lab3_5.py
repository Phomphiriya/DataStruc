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
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def pop(self):
        self.items.pop()
    def push(self,i):
        self.items.append(i)
    def remove(self,i):
        self.items.remove(i)


print("******** Parking Lot ********")
max,member,verb,car = input("Enter max of car,car in soi,operation : ").split()
max,car = int(max),int(car)
member = member.split(',')
s = Stack()

for i in member:
    if i != '0':
        s.push(int(i))

if s.size() < max:
    if verb == 'arrive' and car not in s.items:
        s.push(car)
        print(f"car {car} arrive! : Add Car {car}")
    elif verb == 'arrive' and car in s.items:
        print(f"car {car} already in soi")

    elif verb == 'depart' and car in s.items:
        s.remove(car)
        print(f'car {car} depart ! : Car {car} was remove')
    elif verb == 'depart' and s.size() == 0:
        print(f'car {car} cannot depart : Soi Empty')    
    elif verb == 'depart' and car not in s.items:
        print(f'car {car} cannot depart : Dont Have Car {car}')

elif s.size() >= max:
    if verb == 'depart' and car in s.items:
        s.remove(car)
        print(f'car {car} depart ! : Car {car} was remove')
    else:
        print(f"car {car} cannot arrive : Soi Full")
print(s)

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 5
# car 5 arrive! : Add Car 5
# [1, 2, 3, 4, 5]

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 4 1,2,3,4 arrive 5
# car 5 cannot arrive : Soi Full
# [1, 2, 3, 4]

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 1
# car 1 already in soi
# [1, 2, 3, 4]

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 5 0 depart 3
# car 3 cannot depart : Soi Empty
# []

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 6 2,3,5,7,8 depart 1
# car 1 cannot depart : Dont Have Car 1
# [2, 3, 5, 7, 8]

# ******** Parking Lot ********
# Enter max of car,car in soi,operation : 4 1,3,2 depart 1
# car 1 depart ! : Car 1 was remove
# [3, 2]

