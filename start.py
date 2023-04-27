value = int(input("Enter Number"))
for num in range(1,value+1):
    if num%3 == 0 or num%5 ==0:
        print("fuzz")
    else:  
        print( "*" * num)