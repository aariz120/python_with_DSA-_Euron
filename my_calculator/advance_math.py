import math
def power(base,exponent):
    """this will calculate power"""
    return base**exponent

def square_root(number):
    """this will square of number"""
    if number<0:
        return "cant do this ops"
    return math.sqrt(number)

if __name__=="__main__":
     
    print(square_root(1225))
    print(power(6,3))