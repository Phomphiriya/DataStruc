print("*** Rabbit & Turtle ***")
d,Vr,Vt,Vf = (map(int,input("Enter Input : ").split()))
# print(d,Vr,Vt,Vf)
Sf = Vf*abs(d/(Vr-Vt))
Sf = float(Sf)
print("{:.2f}".format(Sf))

# *** Rabbit & Turtle ***
# Enter Input : 10 1 2 300
# 3000.00

# *** Rabbit & Turtle ***
# Enter Input : 20 2 4 200
# 2000.00