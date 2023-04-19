for x in range(1,100):
    if (x%3==0) and (x%5==0):
        print("FizzBuzz",x)
    elif x%5==0:
        print("Buzz",x)
    elif x%3==0:
        print("fizz",x)
    else :
        print(x)