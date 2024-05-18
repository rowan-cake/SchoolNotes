def validPerimeter(num1,num2,num3):
    """
    BLAH 

    Return:
    (boolean)
    """
    if num1<0 or num2<0 or num3<0:
        return False
    if not (num1+num2)>num3 or not (num1+num3)>num2 or not(num2+num3)>num1:
        return False
    return num1+num2+num3

string = input("Enter three edges")
num1,num2,num3 = map(float,string.split())
# got lazy but wtv
print(validPerimeter(num1,num2,num3))
    
    
