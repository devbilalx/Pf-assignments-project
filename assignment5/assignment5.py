def is_prime(number): 
    if number<2:
        return False

    if not float(number):
        return False


    for i in range(2,number):
        if number%i==0:
            return False
    return True

print(is_prime(6.44))



def output_factor(number):
    for i in range(1,number+1):
        if number%i==0:
            print(i)
    
output_factor(10)