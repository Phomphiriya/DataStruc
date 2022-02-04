class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.high = 1

    def getHigh(self, target):
        if target == None:
            return 0
        return target.high

    def insert(self, data, cur=-123):
        if cur == -123:
            cur = self

        if self.data == None:
            self.data = data
            return self
        if cur == None:
            return Node(data)
        if data < cur.data:
            cur.left = self.insert(data, cur.left)
        elif data > cur.data:
            cur.right = self.insert(data, cur.right)

        cur.high = max(self.getHigh(cur.left), self.getHigh(cur.right)) + 1

        b = self.getHigh(cur.left) - self.getHigh(cur.right)
        if b > 1 or b < -1:
            print("Not Balance, Rebalance!")
        if b > 1 and data < cur.left.data:
            return self.rightRotate(cur)
        if b > 1 and data > cur.left.data:
            cur.left = self.leftRotate(cur.left)
            return self.rightRotate(cur)
        if b < -1 and data < cur.right.data:
            cur.right = self.rightRotate(cur.right)
            return self.leftRotate(cur)
        if b < -1 and data > cur.right.data:
            return self.leftRotate(cur)

        return cur

    def leftRotate(self, cur):
        mid = cur.right
        cur.right = mid.left
        mid.left = cur

        cur.high = max(self.getHigh(cur.left), self.getHigh(cur.right)) + 1
        mid.high = max(self.getHigh(mid.left), self.getHigh(mid.right)) + 1

        return mid

    def rightRotate(self, cur):
        mid = cur.left
        cur.left = mid.right
        mid.right = cur

        cur.high = max(self.getHigh(cur.left), self.getHigh(cur.right)) + 1
        mid.high = max(self.getHigh(mid.left), self.getHigh(mid.right)) + 1

        return mid

    def pri(self, cur, le):
        if cur != None:
            self.pri(cur.right, le+1)
            print(le*"     ", cur.data)
            self.pri(cur.left, le+1)


inp = input("Enter Input : ").split()
root = Node()
for i in inp:
    print("insert : "+str(i))
    root = root.insert(int(i))
    root.pri(root, 0)
    print("===============")