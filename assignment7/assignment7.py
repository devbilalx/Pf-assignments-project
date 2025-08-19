##################        ASSIGNMENT 7 ###########################


def calcualte_sgpa(singleList):
    totalMarks=0
    totalSubject=0

    if singleList is None:
        return None
    if isinstance(singleList,str):
        singleList=[singleList]

    gradesList=["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","F"]


    for userGrade in singleList:
        for realGrade in gradesList:
            if userGrade==realGrade:
                totalSubject=totalSubject+1
                if userGrade=="A+":
                    totalMarks=totalMarks+4.00
                elif userGrade=="A":
                    totalMarks=totalMarks+4.00
                elif userGrade=="A-":
                    totalMarks=totalMarks+3.67
                elif userGrade=="B+":
                    totalMarks=totalMarks+3.33
                elif userGrade=="B":
                    totalMarks=totalMarks+3.00
                elif userGrade=="B-":
                    totalMarks=totalMarks+2.67
                elif userGrade=="C+":
                    totalMarks=totalMarks+2.33
                elif userGrade=="C":
                    totalMarks=totalMarks+2.00
                elif userGrade=="C-":
                    totalMarks=totalMarks+1.67  
                elif userGrade=="D+":
                    totalMarks=totalMarks+1.33
                elif userGrade=="D":
                    totalMarks=totalMarks+1.00
                elif userGrade=="F":
                    totalMarks=totalMarks+0
    

    if totalSubject==0:
        return None
    else:
        scGpa=totalMarks/totalSubject
        return scGpa


def calculate_sgpa_weighted(singleList,creditHour):
    totalCredit=0
    sumGrade=0

    if isinstance(singleList,str) or isinstance(creditHour,int):
        singleList=[singleList]
        creditHour=[creditHour]

    if len(singleList)!=len(creditHour):
        return None

    

  
    for i in range(len(singleList)):
        convert=gradeEQ(singleList[i])
        credit=creditHour[i]

        sumGrade=sumGrade+ (convert*credit)
        totalCredit+=credit
    
    if totalCredit==0:
        return None
    else:
        return sumGrade/totalCredit


def gradeEQ(grade1):
        if grade1 == 'A+':
            return 4.00
        elif grade1 == 'A':        
            return 4.00
        elif grade1 == 'A-':
            return 3.67
        elif grade1 == 'B+':
             return 3.33
        elif grade1 == 'B':
            return 3.00
        elif grade1 == 'B-':
            return 2.67
        elif grade1 == 'C+':
            return 2.33
        elif grade1 == 'C':
            return 2.00
        elif grade1 == 'C-':
            return 1.67
        elif grade1 == 'D+':
            return 1.33
        elif grade1 == 'D':
            return 1.00
        elif grade1 == 'F':
            return 0.00
    

    


print(calculate_sgpa_weighted("C-", 4))
    
    