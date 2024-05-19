import numpy as np
def getNumsFromUser():
    """
    Effects: 
    gets numbers from user and stores it in an array (or vector not sure yet)
    two inputs from user size of array and each number

    Returns:
    numbers(list): list of the numbers
    """
    size = int(input("Enter number of students:"))
    numbers = np.array([])
    print("Enter student Grades")
    for i in range(size):
        numbers = np.append(numbers,int(input()))        
    return numbers

if __name__ == "__main__":
    numbers = getNumsFromUser()
    print(numbers)
