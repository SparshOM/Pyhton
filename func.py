def reverse_value(value):
#    if type(value)==list or type(value)== str:
    reverse = value[::-1]
#    else:
#        temp = str(value)
#        reverse_value= value[::-1]
    return reverse

s = []
s = str(input("Enter Value "))
print(reverse_value(s))