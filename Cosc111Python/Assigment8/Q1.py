def matrixSum(matrix1,matrix2):
    """
    cmon now dawg
    """
    matrix3 = []
    if len(matrix1) != len(matrix2):
        return "NOT SAME SIZE"
    for i in range(len(matrix1)):
            if len(matrix1[i]) != len(matrix2[i]):
                    return "NOT SAME SIZE"
    for i in range(len(matrix1)):
        matrix3.append([])
        for j in range(len(matrix1[i])):
                matrix3[i].insert(j,matrix1[i][j]+matrix2[i][j])
    return matrix3


