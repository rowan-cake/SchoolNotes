from Q1 import getNumsFromUser
def isSorted(list):
    """
    Effects:
    checks if list was sorted or not

    Paremeters:
    list(numpyArray): the list of numbers the user inputs

    Returns:
    boolean
    """

    min = list[0] # Make minum the first number in list
    for i in range(list.size):
        if list[i]<min:
            return False
        else:
            min = list[i]
    return True

if __name__ == "__main__":
    if isSorted(getNumsFromUser()) == True:
        print("List is sorted")
    else:
        print("List not sorted")