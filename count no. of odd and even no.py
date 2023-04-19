li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
odd = 0
even = 0
for x in li:
    if x %2==1:
        odd = odd+1
    else:
        even=even+1
print("Odd-",odd ," Even-",even)