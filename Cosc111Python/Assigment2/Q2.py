def roadTripCalculator(fc,d,fe):
    """
    Effects:
    Calculatest the cost of the roadtrip

    Parmeters:
    fc(float): fuel cost(price of gas, $ per gallon)
    d(float): distance(miles)
    fe(float): average miles per gallon 

    Returns:
    float: price
    """
    price = (d/fe)*fc
    return price

miles = float(input("Enter the driving distance in miles"))
fe = float(input("Enter miles per gallon"))
fc = float(input("Enter price in $ per gallon"))
print("The cost of driving is $",roadTripCalculator(fc,miles,fe))