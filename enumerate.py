list1=[10,20,30,40,50,60,70,80,90]
key = float(input("Enter->"))
for value,value2 in enumerate(list1):
# enumerate for index format- key,value
    if key==value2:
        print("Present at",value)
        break
    else:
        continue