import math

def is_prime_num(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    
    return True