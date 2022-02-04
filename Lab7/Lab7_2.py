from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        p = Node(data)
        if self.root is None:
            self.root = p
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = p
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = p
                        break
                    curr = curr.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def findBelow(self, node, k):
        global ls
        if node != None:
            self.findBelow(node.left, k)
            if node.data < k:
                # print(node.data,end=" ")
                ls.append(node.data)
            self.findBelow(node.right, k)

ls =[]
T = BST()
inp = input("Enter Input : ").split("|")
for i in inp[0].split():
    i = int(i)
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(f'Below {inp[1]} : ',end='')
T.findBelow(root, int(inp[1]))
if len(ls) == 0:
    print("Not have")
else:
    print(*ls,end='')