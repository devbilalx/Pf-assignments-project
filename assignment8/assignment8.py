# Assignment 8 

def find_cumulative_marks(result):
    newList=[]
    for eachResult in result:
        marks=0
        for i in range(2,len(eachResult)):
            value=eachResult[i]
            if value is None:
                value=0    
            marks+=value
        newList.append((eachResult[0],eachResult[1],marks))
    return newList

v=find_cumulative_marks( [
 ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
 ('p10111', 'Mudasser Farooq', 14, 28.5, 83, 76),
 ('p101113', 'Tamleek Ali', 87, None, 1.6)
]

)
print(v)



def find_top_student(result):

    cumulativeMarks=find_cumulative_marks(result)

    topStudent=cumulativeMarks[0]

    for eachResut in range(1,len(cumulativeMarks)):
        if cumulativeMarks[eachResut][2]>topStudent[2]:
            topStudent=cumulativeMarks[eachResut]
    
    return ((topStudent[0],topStudent[1]))



v=find_top_student([
 ('p10111', 'Mudasser Farooq', 14, 28.5, 83, 76),
 ('p101113', 'Tamleek Ali', 87, None, 1.6),
 ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99)
])

print(v)  






def find_top_student(result):
    cumulative=find_cumulative_marks(result)
    newList=[]
    marks=-1

    if cumulative is None:
        return None
    
    if cumulative==[]:
        return []

    for eachResult in cumulative:
        if eachResult[2]>marks:
            marks=eachResult[2]
            newList.append((eachResult[0],eachResult[1]))
        elif eachResult[2]==marks:
            newList.append((eachResult[0],eachResult[1]))

    return newList

print(find_top_student( [
('p101111', 'Ali Khayam', 64, 10),
('p101112', 'Mudasser Farooq', 50, 24),
('p101113', 'Tamleek Ali', 10, 20)
]))
 

