l =[]
for value in range(1500,2700):
    if (value %3 == 0) and (value % 5==0):
        l.append(value)
print(l)