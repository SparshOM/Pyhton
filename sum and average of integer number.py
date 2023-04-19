sum=0
n = int(input("Enter Number"))
for x in range(1,n+1):
    sum = sum + x
avg = sum/n
print("sum->",sum,"avg->",avg)