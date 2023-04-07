list1=[10,20,30,40,50,60,70,80,90]
key = float(input("Enter->"))
for value in list1:
    if key==value:
        print("Present")
        break
    else:
        continue
else:
    print("Not Present")

l = [10,20,30,40,50,60]
key = 40
for value in l:
    if value == key:
        print("Element found")
        break
    else:
        continue