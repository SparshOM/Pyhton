numm =input("Type Number-> ")
try:
    num= int(numm)
except:
    num = -1
if num > 0:
    print("A Number")
elif num ==0:
    print("Zero")
else:
    print(num)
    print("Not A Number")
