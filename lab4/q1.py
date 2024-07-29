import os
import math

def find_primitive_roots(n):
    if n < 2:
        return []

    def is_primitive_root(root, n):
        required_set = set(num for num in range(1, n) if math.gcd(num, n) == 1)
        actual_set = set(pow(root, powers, n) for powers in range(1, n))
        return required_set == actual_set

    primitive_roots = [num for num in range(1, n) if is_primitive_root(num, n)]
    return primitive_roots

number = int(input("Enter a number: "))
if 1000 <= number <= 2000:
    print("The number is between 1000 and 2000. Shutting down the system...")
else:
    roots = find_primitive_roots(number)
    if roots:
        print(f"The primitive roots of {number} are: {roots}")
    else:
        print(f"There are no primitive roots for {number}.")
