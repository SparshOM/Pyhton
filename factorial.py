n = int(input("Enter Number"))
fac =1
if n==0 or n <0:
    print("Enter Valid Number")
else:
    for x in range(1,n+1):
        fac = fac*x
        n = n-1
    print(fac)