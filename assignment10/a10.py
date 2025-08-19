


import os

def line_count(dir,name,countEmpty=False):
    fileName=os.path.join(dir,name)

    count=0
    with open (fileName,'r') as f:
        

        for line in f:
            if not countEmpty or line.strip():
                count+=1
        
    return count


def character_count(dir,name,skipSpaces=False):

    fileName=os.path.join(dir,name)

    charCount=0

    with open( fileName, 'r') as f:

        for eachLine in f:
            if skipSpaces:
                eachLine="".join(eachLine.split())
            charCount+=len(eachLine)
    
    return charCount







# line_count('ictt//assignment10','essay.txt',True)
# print(character_count('ictt//assignment10','essay.txt',True))