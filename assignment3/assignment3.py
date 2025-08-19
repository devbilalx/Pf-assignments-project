## assignment 3


def average(x,y):
    return ((x+y)/2)  




def improve_guess(x,a):
    return average(a,x/a)


def abs(x):
    if x<0:
        return -x
    else:
        return x



def sqrt(x,guess=0):
    if good_enough(guess,x):
        return round(guess,5)
    else:
        new_guess=improve_guess(x,guess)
        return sqrt(x,new_guess)




def good_enough(guess,x):

    if abs(guess*guess-x)<0.000001:
        return True
    else:
        return False

 



