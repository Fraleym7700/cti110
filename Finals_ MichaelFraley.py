# Program that will count how many bugs the bug collector got
# 10/8/19
# CTI-110 P4T2 - Bug Collector
# Michael Fraley
#
# initialize the accumulator


def getGrade():
    total = 0
    gradesInput= int(input("How many grades would you like to input?"))
    for grades in range(gradesInput):
        print("Enter in your grade", grades)
        newGrade = int(input())
        total += newGrade
        score = total/gradesInput
    A_score = (90)
    B_score = (80)
    C_score = (70)
    D_score = (60)

    gradeTotal = score
    if gradeTotal >= A_score:
        print('Your grade is A and your grade total is', format(gradeTotal,".2f"))
    elif gradeTotal >= B_score:
        print('Your grade is B and your grade total is', format(gradeTotal,".2f"))
    elif gradeTotal >= C_score:
        print('Your grade is C and your grade total is', format(gradeTotal,".2f"))
    elif gradeTotal >= D_score:
        print('Your grade is D and your grade total is', format(gradeTotal,".2f"))
    else:
        print('Your grade is F and your grade total is', format(gradeTotal,".2f"))
getGrade()

