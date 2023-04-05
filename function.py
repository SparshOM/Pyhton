def function(days,rate1):
#    days = input("Enter Days->")
#    rate1 = input("Enter Rate->")
    try:
        day = float(days)
        rate = float(rate1)
        print(day*rate)
    except:
        print("Not A number")

function(days=input("Enter Days->"),rate1=input("Enter Rate->"))

