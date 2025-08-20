import os

# Part A + B

def line_count(dir,name,countEmpty=False):
    fileName=os.path.join(dir,name)

    count=0
    with open (fileName,'r') as f:
        

        for line in f:
            if not countEmpty or line.strip():
                count+=1
        
    return count

# Part C + D
def character_count(dir,name,skipSpaces=False):

    fileName=os.path.join(dir,name)

    charCount=0

    with open( fileName, 'r') as f:

        for eachLine in f:
            if skipSpaces:
                eachLine="".join(eachLine.split())
            charCount+=len(eachLine)
    
    return charCount

# Part E

def move_lines(inputPath,outputPath,lines_to_move):
    try:
        fileToRead=inputPath
        fileToWrite=outputPath
        with open( fileToRead,'r') as f:
            with open(fileToWrite,'w') as w:
                count=0
                for eachLine in f:
                    count+=1
                    if count<=lines_to_move:
                        w.write(eachLine)
    except:
        FileNotFoundError
        print("File Directory to read data is wrong")






# print(line_count('itc//assignment10','essay.txt',False))
# print(character_count('itc//assignment10','essay.txt',False))

# move_lines('itc\\assignment10\\essay.txt','itc\\assignment10\\new.txt',11)
