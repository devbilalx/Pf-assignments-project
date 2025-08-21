def is_prime(number): 
    if number<2:
        return False
    

    if isinstance(number,float):
        if number % 1==0:
            number=int(number)
        else:
            return False

    for i in range(2,int(number)):
        if number%i==0:
            return False
    return True

print(is_prime(3))



def output_factors(number):
    factors=[]
    for i in range(1,number+1):
        if number%i==0:
            factors.append(i)
    for factor in factors:
        print(factor)

