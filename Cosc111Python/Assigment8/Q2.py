def sumCollumn(matrix,collumn):
    """
    Im good off that
    """
    sum = 0
    collumn -=1 # to make it right for the brain
    for i in range(len(matrix)):
        sum += matrix[i][collumn]
    return sum