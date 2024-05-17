def windchill(temp,windSpeed):
    """
    Effects: 
    calculates the wind chill using the formula given in the pdf

    Parameters:
    temp(float): Temparature
    windSpeed(float): The wind speed

    Returns:
    windchill(float)
    """
    twc = 35.74 + 0.6215*temp-35.75*windSpeed**0.16+0.4275*temp*windSpeed**0.16
    return twc
if __name__ == "__main__":
    temp = float(input("Enter the temperature in Fahrenheit between -58F and 41F:"))
    windSpeed = float(input("Enter the wind speed in miles per hour (must be greater than or equal to 2):"))  
    print("The wind chill index is ", windchill(temp,windSpeed))