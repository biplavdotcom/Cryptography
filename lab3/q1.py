import random

def miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    def is_composite(a):

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    
    for _ in range(k):
        a = random.randint(2, n - 2)
        if is_composite(a):
            return False
    
    return True

n = 341   
k = 5    
result = miller_rabin(n, k)
print(f"{n} is {'probably prime' if result else 'composite'}")