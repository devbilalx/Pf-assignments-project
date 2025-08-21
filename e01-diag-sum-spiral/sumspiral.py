
def get_diag_sum(n):
    if n%2==0:
        return None
    else:
        
        # diagonal=n*n
        sum=1
        current=1
        for i in range(2,n,2):
            for y in range(4):
                current+=i
                sum+=current
        return sum


    

print(get_diag_sum(5))