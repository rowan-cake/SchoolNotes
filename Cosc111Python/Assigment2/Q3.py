from math import sqrt

def distance(x1,y1,x2,y2):
    """
    Effects: Calculates teh distance between two poitns

    Parameters:
    x1(float):
    y1(float):
    x2(float):
    x2(float):

    Returns: 
    A distance
    """
    return sqrt((x2-x1)**2+(y2-y1)**2)
if __name__ == "__main__":
    x1 = float(input("Enter x1 and y1"))    
    y1 = float(input())
    x2 = float(input("Enter x2 and y2"))
    y2 = float(input())

    print("The distance of the two points is ",distance(x1,y1,x2,y2))