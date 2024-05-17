import numpy as np
def randomPlate():
    """
    Effects:
    Make a random 7 digit string of capital letters and numbers

    Parameters:
    null

    Returns:
    plate(String): The plate    
    
    """
    plate = ""
    #stars from 0 and goes till i<3 is false
    for i in range(3): 
        plate += chr(np.random.randint(65,91))
    for i in range(4):
        plate+=str(np.random.randint(0,10))
        print(i)
    return plate

if __name__ == "__main__":
    print("The random plate number is: ",randomPlate())