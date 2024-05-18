import numpy as np

def computerRPS():
    # rand int from 0-2
    return np.random.randint(0,3)


def stringPrinter(choice):
    """
    Effects print the string at the end of the game

    Paremeteres:
    choice(int): users choice

    Returns:
    string

    """
    map = {0:"scissor",1:"rock",2:"paper"}
    cmptChoice = computerRPS()
    cmptString = map.get(cmptChoice)
    choiceString = map.get(choice)
    if cmptChoice>choice or choice==2 and computerRPS==0:
        return "The computer is %s. You are %s. You Lost" % (cmptString,choiceString)
    elif cmptChoice == choice:
        return "TIE"
    else:
        return "The computer is %s. You are %s. You won" % (cmptString,choiceString) 

choice = int(input("scissor (0), rock(1), paper(2):"))
print(stringPrinter(choice))