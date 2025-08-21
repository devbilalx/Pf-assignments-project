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


def output_prime_factor(n):

    if n<0:
        n=abs(n)

    if isinstance(n,float):
        n=int(round(n))


    factors=[]

    for i in range(2,n+1):
        while n%i==0 and is_prime(i):
            print(i)
            n=n//i


def get_nth_prime(n):
    if isinstance(n,float):
        return None
    
    if n<1:
        return None
    
    prime=0
    count=0
    while True:
        prime=prime+1

        if is_prime(prime):
            count+=1
            if count==n:
                return prime

print(get_nth_prime(4))