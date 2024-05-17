import numpy as np
def digitalRoot(num):
    """
    Effects:
    Given a 3 digit number it gets teh digital root of that number

    Parameters:
    num(integer): the number given

    Returns:
    root(integer): the digital root
    """
    root = num%10 #the last digit 
    root+= (num//10)%10 # the middle digit
    root+= num//100 # fisrt digit
    return root

   
if __name__ == "__main__":
    number = int(input("Entere a 3 digit number"))
    print("digital root of %d is %d" % (number,digitalRoot(number)))