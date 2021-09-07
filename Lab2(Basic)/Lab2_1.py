class Calculator :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self):
        ansAdd = self.x + self.y
        return ansAdd
    def __sub__(self):
        ansSub = self.x - self.y
        return ansSub
    def __mul__(self):
        ansMu = self.x * self.y
        return ansMu
    def __truediv__(self):
        ansDiv = self.x / self.y
        return ansDiv


x,y = input("Enter num1 num2 : ").split(",")
c = Calculator(int(x),int(y))
print(c.__add__(),c.__sub__(),c.__mul__(),c.__truediv__(),sep = "\n")

# Enter num1 num2 : 5,5
# 10
# 0
# 25
# 1.0

# Enter num1 num2 : 20,5
# 25
# 15
# 100
# 4.0


