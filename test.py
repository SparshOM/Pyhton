print(ord('A'))
fac = 1
def factorial(num):
    for x in range(1,num):
        fac = fac* x
        num = num-1
    return fac

faco= factorial(9)
print(faco)
