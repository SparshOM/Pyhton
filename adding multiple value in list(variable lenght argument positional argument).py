def add_value(*agur):
    l= []
    for value in agur:
        l.append(value)
    return l
    
result = add_value(100,200,300,400)
print(result)
result = add_value(100,200,600,700)
print(result)
result = add_value(800,900)
print(result)