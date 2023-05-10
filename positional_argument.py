def linear_search(li,value):
    for num in li:
        if value == num:
            return True
    else:
           return False
    
li = [100,200,300,400,500]
value= int(input("Enter Value "))
print(linear_search(li,value))