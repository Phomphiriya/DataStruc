print("*** Rabbit & Turtle ***")
d,Vr,Vt,Vf = (map(int,input("Enter Input : ").split()))
# print(d,Vr,Vt,Vf)
Sf = Vf*abs(d/(Vr-Vt))
Sf = float(Sf)
print("{:.2f}".format(Sf))