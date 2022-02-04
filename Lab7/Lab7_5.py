class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
        return self.root

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node.data)
            self.print_tree(node.left, level + 1)

def inorder(curr):
    if curr:
        if curr.left is not None or curr.right is not None:
            print("(",end='')
        inorder(curr.left)
        print(curr.data , end='')
        inorder(curr.right)
        if curr.left is not None or curr.right is not None:
            print(")",end='')

def preorder(curr):
    if curr is not None:
        print(curr.data, end='')
        preorder(curr.left)
        preorder(curr.right)

inp = input("Enter Postfix : ")
tree = BST()
s = Stack()
for i in inp:
    if i in '+-*/':
        operator1 = s.pop()
        operator2 = s.pop()
        s.push(Node(i, operator2, operator1 ))
    else:
        s.push(Node(i))
print("Tree :")
tree.root = s.pop()
tree.print_tree(tree.root)
print("--------------------------------------------------")
print(f'Infix : ',end='')
inorder(tree.root)
print(f'\nPrefix : ' , end='')
preorder(tree.root)