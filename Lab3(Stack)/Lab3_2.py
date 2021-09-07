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
    def peek(self):
        return self.items[-1]
    def pop(self):
        self.items.pop()
    def push(self,i):
        self.items.append(i)

def isMatch(i,j):
    if i == "(" and j == ")":
        return True
    elif i == "{" and j == "}":
        return True
    elif i == "[" and j == "]":
        return True

inp = input("Enter expresion : ")
s = Stack()
OpenB = ["(","{","["]
CloseB = [")","}","]"]
OpenCheck = 0
CloseCheck = 0

for i in inp:
    if i in OpenB:
        OpenCheck +=1
    elif i in CloseB:
        CloseCheck +=1
try:
    for i in inp:
        if i in OpenB:
            s.push(i)
        elif i in CloseB:
            last = s.peek()
            if isMatch(last,i):
                s.pop()

    print(inp,end=' ')
    if s.isEmpty():
        print("MATCH")
    elif OpenCheck > CloseCheck:
        print("open paren excess   {} : {}".format(s.size(),''.join(s.items)))
    else:
        print("Unmatch open-close")
except:
    print(inp+" close paren excess")

# Enter expresion : [[)))))
# [[))))) Unmatch open-close  

# Enter expresion : [[))
# [[)) Unmatch open-close 

# Enter expresion : (())))
# (()))) close paren excess

# Enter expresion : )}]
# )}] close paren excess

# Enter expresion : (((
# ((( open paren excess   3 : (((

# Enter expresion : (a+c)(a-b)*c(-a
# (a+c)(a-b)*c(-a open paren excess   1 : (