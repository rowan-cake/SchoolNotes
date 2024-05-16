
def aceleration(v1,v0,t):
    """
    Takes in a starting velocity and a final velocity along
    with a time and calculates the aceraltion over that time
    change

    Parameters:
    v1(float): final velocity
    v0(float): strat velocity
    t(float): time

    Returns:
    float: a
    """
    a = (v1-v0)/ t 
    return a

print("Enter v0, v1, and t:")
v0 = float(input())
v1 = float(input())
t = float(input())

a = aceleration(v1,v0,t)
print("The average aceleration is ",a)