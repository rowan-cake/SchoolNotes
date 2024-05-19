from Q1 import getNumsFromUser

def showLetterGrades(grades):
    """
    Effects: 
    Assigns a grade based on what the grade was and the
    top grade

    Paremeteres:
    grades(list): the grades in question 

    Returns:
    nothing (just prints)

    """
    max = grades.max()
    # hMap = {max-10:"A",max-20:"B",max-30:"C",max-40:"D"}
    count = 0
    grade = ""
    for mark in grades:
        count+=1
        if mark >= max-10:
            grade = "A"
        elif mark >= max-20:
            grade = "B"
        elif mark >= max-30:
            grade = "C"
        elif mark >= max-40:
            grade = "D"
        else:
            grade = "F" 
        print("Student %d is %d and grade is %s" % (count,mark,grade))

if __name__ == "__main__":
    showLetterGrades(getNumsFromUser())