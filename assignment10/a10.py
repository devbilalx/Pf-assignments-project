


import os

def line_count(dir,name,countEmpty=False):
    fileName=os.path.join(dir,name)

    count=0
    with open (fileName,'r') as f:
        

        for line in f:
            if not countEmpty or line.strip():
                count+=1
        
    print(count)


def character_count(dir,name,skipSpaces=False):

    fileName=os.path.join(dir,name)

    wordCount=0

    with open( fileName, 'r') as f:

        for eachLine in f:
            if not skipSpaces or eachLine.strip():

                wordCount+=len(eachLine)
    print(wordCount)





line_count('ictt//assignment10','essay.txt',True)
character_count('ictt//assignment10','essay.txt')