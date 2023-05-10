import random

def Genrate_Password(length=8):
    l= ['!','@','#','$','%']
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    digits= random.randint(10000,99999)
    special = random.choice(l)
    password = upper+lower+str(digits)+special
    len = random.sample(password,length)
    password = ("").join(len)

    return password
#length = int(input("Enter"))
print(Genrate_Password())  