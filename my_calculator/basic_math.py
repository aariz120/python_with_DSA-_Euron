def add(a,b):
    """ this will add two numbers"""
    return a+b

def substract(a,b):
    """ this will give you substraction of two numbers"""
    return a-b

def multiply(a,b):
    """this will give multiplication of two numbers"""
    return a*b

def divide(a,b):
    """this will divide two numbers"""
    if b==0:
        return "cant do this ops"
    return a/b


if __name__=="__main__":
    
    print("testing...")
    print(add(4,6))
    print(substract(65,34))


