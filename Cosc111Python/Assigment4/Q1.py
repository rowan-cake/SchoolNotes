def vowel(char):
    """
    Effects: tells you wheter a char is a vowel,consonat or neitehr

    Paremeters: 
    char(chr): the charater

    Returns:
    descion(str): what type of charatrer it is
    """
    numberValue = ord(char)
    hMap = {'a':' vowel',
            'e':' vowel',
            'i':' vowel',
            'o':' vowel',
            'u':' vowel'}
    
    if numberValue >= 97 and numberValue <= 122:
        descion = hMap.get(char," consonat")
        return descion
    else:
        descion = "n invalid input"
        return descion  

if __name__ == "__main__":
    # dont have to cast as a char there
    chararter = input("Enter a letter:")
    print("%s is a%s" % (chararter,vowel(chararter)))

    