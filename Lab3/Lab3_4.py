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
        return self.items.pop()
        return
    def push(self,i):
        self.items.append(i)

def checkrank(peek,new):
    rank = {"+":1 ,"-":1 ,"*":2 ,"/":2,"(":3}
    if rank.get(peek) >= rank.get(new):
        return True
    else:
        return False

def infixtopostfix(inp):
    s = Stack()
    operator = ["(","+","-","*","/"]
    ans = ""
    for i in inp:
        if i in operator:
            if not s.isEmpty() and checkrank(s.peek(),i):
                while not s.isEmpty() and s.peek() != '(' and checkrank(s.peek(),i):
                    ans += s.pop()
            s.push(i)
        elif i == ')':
            while not s.isEmpty() and s.peek() != '(':
                ans += s.pop()
            s.pop()
        else:
            ans += i
    while not s.isEmpty():
        ans += str(''.join(s.pop()))
    return ans


print(" ***Infix to Postfix***")
inp = input("Enter Infix expression : ")
print("PostFix : ")
print(infixtopostfix(inp))

#  ***Infix to Postfix***
# Enter Infix expression : a-b-c-d
# PostFix : 
# ab-c-d-

#  ***Infix to Postfix***
# Enter Infix expression : (((a-b)-c)-d)
# PostFix : 
# ab-c-d-

#  ***Infix to Postfix***
# Enter Infix expression : (a-(b-(c-d)))
# PostFix : 
# abcd---