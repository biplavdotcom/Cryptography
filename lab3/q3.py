def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def power_mod(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def find_prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        while (n % i) == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return factors

def find_primitive_roots(p):
    if p == 2:
        return [1]
    
    phi = p - 1
    prime_factors = find_prime_factors(phi)
    
    primitive_roots = []
    for g in range(2, p):
        is_primitive_root = True
        for factor in prime_factors:
            if power_mod(g, phi // factor, p) == 1:
                is_primitive_root = False
                break
        if is_primitive_root:
            primitive_roots.append(g)
    
    return primitive_roots
p = 23
primitive_roots = find_primitive_roots(p)
print(f"Primitive roots of {p} are: {primitive_roots}")