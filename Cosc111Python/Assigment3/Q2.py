import numpy as np
def operator(num):
    """
    Effects:
    Takes the fraction part and the real part and seprates them 
    and returns both values 

    Paremeters:
    num(float): number in question

    Returns:
    A tuple of a interger and a deicmal part
    """
    int = np.floor(num)
    frac = num-int
    return int,frac

if __name__ == "__main__":
    number = float(input("Enter a real number"))
    #store the two values by themselves
    real,frac = operator(number)
    # REalized i mighht not need that function 
    print("Interger part:",real)
    print("Fraction part:",frac)
