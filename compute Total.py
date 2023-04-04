def computeTotal(days,rate):
    total= days*rate
    return total
try:    
    days = float(input("Enter days->"))
    rate = float(input("Enter Rate->"))
    print("Total ", computeTotal(days,rate))
except:
    print("Enter Only Number")