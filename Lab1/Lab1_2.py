high,weight = input("Enter your High and Weight : ").split()
high = float(high)
weight = int(weight)
#  print(high,weight)
bmi = (weight/(high*high))
# print (bmi)
if bmi >= 30:
    print("Fat")
elif bmi >= 25:
    print("Getting Fat")
elif bmi >= 23:
    print("More than Normal Weight")
elif bmi >= 18.50:
    print("Normal Weight")
else:
    print("Less Weight")
