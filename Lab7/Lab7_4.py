class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
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
        
    def delete(self,r, data):
        def minValueNode(node):
            cur = node
            while(cur.left is not None):
                cur = cur.left
            return cur
        self.ishave = False
        if self.root and not self.root.left and not self.root.right and self.root.data == data:
            self.root = None
            self.ishave = True
            return 
        if not r: 
            return r
        if data < r.data:
            r.left = self.delete(r.left , data  )
        elif data > r.data:
            r.right = self.delete(r.right , data  )
        else:
            self.ishave = True
            if not r.left:
                temp = r.right
                if r == self.root:
                    self.root = r.right
                r = None
                return temp
            elif not r.right:
                temp = r.left
                if r == self.root:
                    self.root = r.left
                r = None
                return temp
            temp = minValueNode(r.right)
            r.data = temp.data
            r.right = self.delete(r.right , temp.data )
        return r

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    data = i.split()
    if data[0] == 'i':
        tree.insert(int(data[1]))
        print(f'insert {data[1]}')
        printTree90(tree.root)
    if data[0] == 'd':
        tree.delete(tree.root , int(data[1]))
        print(f'delete {data[1]}')
        if not tree.ishave: print('Error! Not Found DATA')
        printTree90(tree.root)