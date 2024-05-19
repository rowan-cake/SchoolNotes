from Q1 import matrixSum
from Q2 import sumCollumn 
class PreEnter:
    @staticmethod
    def displayArray(m):
        for row in m:
            for element in row:
                print(element, end=" ")
            print()

    @staticmethod
    def main():
        m1 = [
            [14, 11, 13, 12],
            [18, 15, 13, 13],
            [19, 16, 15, 17]
        ]
        m2 = [
            [54, 53, 51, 52],
            [51, 59, 52, 56],
            [53, 54, 52, 58]
        ]
        print("First array:")
        PreEnter.displayArray(m1)
        print("Second array:")
        PreEnter.displayArray(m2)
        print("THe addition of the arrays")
        PreEnter.displayArray(matrixSum(m1,m2))
        print("the sume of the first column in the first array is", sumCollumn(m1,1))


if __name__ == "__main__":
    test = PreEnter()
    test.main()
