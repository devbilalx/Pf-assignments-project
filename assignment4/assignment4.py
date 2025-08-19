
# Assignment 4

# Part a
def get_grade(marks):

    if marks>=90:
        return "A+" 
    elif marks>=86:
        return "A"
    elif marks>=82:
        return "A-"
    elif marks>=78:
        return "B+"
    elif marks>=74:
        return "B"
    elif marks>=70:
        return "B-"
    elif marks>=66:
        return "C+"
    elif marks>=62:
        return "C"
    elif marks>=58:
        return "C-"
    elif marks>=54:
        return "D+"
    elif marks>=50:
        return "D"
    else:
        return "F"
    

# Part b
    

def calculate_sgpa(grade1, grade2, grade3):
    total_marks = 0
    total_number_of_subjects = 0

    if grade1 != 'nothing':
        total_number_of_subjects += 1  
        if grade1 == 'A+':
            total_marks += 4.00
        elif grade1 == 'A':
            total_marks += 4.00
        elif grade1 == 'A-':
            total_marks += 3.67
        elif grade1 == 'B+':
            total_marks += 3.33
        elif grade1 == 'B':
            total_marks += 3.00
        elif grade1 == 'B-':
            total_marks += 2.67
        elif grade1 == 'C+':
            total_marks += 2.33
        elif grade1 == 'C':
            total_marks += 2.00
        elif grade1 == 'C-':
            total_marks += 1.67
        elif grade1 == 'D+':
            total_marks += 1.33
        elif grade1 == 'D':
            total_marks += 1.00
        elif grade1 == 'F':
            total_marks += 0.00
    
    if grade2 != 'nothing':
        total_number_of_subjects += 1
        if grade2 == 'A+':
            total_marks += 4.00
        elif grade2 == 'A':
            total_marks += 4.00
        elif grade2 == 'A-':
            total_marks += 3.67
        elif grade2 == 'B+':
            total_marks += 3.33
        elif grade2 == 'B':
            total_marks += 3.00
        elif grade2 == 'B-':
            total_marks += 2.67
        elif grade2 == 'C+':
            total_marks += 2.33
        elif grade2 == 'C':
            total_marks += 2.00
        elif grade2 == 'C-':
            total_marks += 1.67
        elif grade2 == 'D+':
            total_marks += 1.33
        elif grade2 == 'D':
            total_marks += 1.00
        elif grade2 == 'F':
            total_marks += 0.00

    if grade3 != 'nothing':
        total_number_of_subjects += 1  
        if grade3 == 'A+':
            total_marks += 4.00
        elif grade3 == 'A':
            total_marks += 4.00
        elif grade3 == 'A-':
            total_marks += 3.67
        elif grade3 == 'B+':
            total_marks += 3.33
        elif grade3 == 'B':
            total_marks += 3.00
        elif grade3 == 'B-':
            total_marks += 2.67
        elif grade3 == 'C+':
            total_marks += 2.33
        elif grade3 == 'C':
            total_marks += 2.00
        elif grade3 == 'C-':
            total_marks += 1.67
        elif grade3 == 'D+':
            total_marks += 1.33
        elif grade3 == 'D':
            total_marks += 1.00
        elif grade3 == 'F':
            total_marks += 0.00
    
    if total_number_of_subjects == 0:
        return 0.0

    sgpa = total_marks / total_number_of_subjects
    return sgpa

print(calculate_sgpa('A','A','A'))


 