def twoUpperCaseChars(plate):
    """
    Effects: Checks if the first two chars are upper case and
    correct

    Paremeters:
    plate(Str): the plate number

    Returns:
    (boolean): true or flase    
    """
    firstChar = ord(plate[0])
    secondChar = ord(plate[1])
    # if the char is out if bounds of the capitals
    if (firstChar<65 or firstChar>97) or (secondChar<65 or secondChar>97):
        return False 
    else:
        return True
    

def twoNumbers(plate):
    """
    Effects: Checks if the last two chars are numbers

    Paremeters:
    plate(Str): the plate number

    Returns:
    (boolean): true or flase    
    """
    lastChar = ord(plate[4])
    fourthChar = ord(plate[3])
    if (lastChar>57 or lastChar<48) or (fourthChar>57 or fourthChar<48):
        return False
    else:
        return True 


def plateIsValid(plate):
    if len(plate) != 5:
        return False
    elif plate[2] != "-":
        return False
    elif (twoNumbers(plate) == False) or (twoUpperCaseChars == False):
        return False
    else:
        return True
    
if __name__ == "__main__":
    plate = input("Enter a valid plate number:")
    
    
    if plateIsValid(plate) == True:
        boolean = "valid"
    else: 
        boolean = "invalid"
    print("%s is an %s plate number" % (plate,boolean))