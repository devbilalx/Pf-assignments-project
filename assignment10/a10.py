


import os

def line_count(dir,name,countEmpty=False):
    fileName=os.path.join(dir,name)

    count=0
    with open (fileName,'r') as f:
        

        for line in f:
            if not countEmpty or line.strip():
                count+=1
        
    print(count)




