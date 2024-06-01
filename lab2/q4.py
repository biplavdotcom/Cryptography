# Permuted Choice 1 (PC-1) Table
pc1_table = [
    57, 49, 41, 33, 25, 17,  9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4
]

# Permuted Choice 2 (PC-2) Table
pc2_table = [
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Number of left shifts per round
left_shifts = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

def permute(input_block, permutation_table):
    return [input_block[i - 1] for i in permutation_table]

def left_shift(bits, shift_count):
    return bits[shift_count:] + bits[:shift_count]

def generate_subkeys(initial_key):
    # Apply PC-1 to the initial key to get 56-bit key
    permuted_key = permute(initial_key, pc1_table)
    
    # Split the key into two 28-bit halves
    left_half = permuted_key[:28]
    right_half = permuted_key[28:]
    
    subkeys = []
    for shift_count in left_shifts:
        # Shift both halves
        left_half = left_shift(left_half, shift_count)
        right_half = left_shift(right_half, shift_count)
        
        # Combine halves and apply PC-2 to get the subkey
        combined_key = left_half + right_half
        subkey = permute(combined_key, pc2_table)
        subkeys.append(subkey)
    
    return subkeys

def main():
    # Example 64-bit key (8 bytes)
    initial_key = [
        0, 0, 0, 1, 0, 0, 1, 1,
        0, 0, 1, 1, 0, 1, 0, 0,
        0, 1, 0, 1, 1, 0, 1, 1,
        0, 1, 1, 1, 1, 0, 0, 1,
        1, 0, 0, 1, 1, 0, 0, 0,
        1, 0, 1, 0, 1, 1, 1, 0,
        1, 1, 0, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 0, 1, 0
    ]
    
    # Generate the 16 subkeys
    subkeys = generate_subkeys(initial_key)
    
    for i, subkey in enumerate(subkeys, 1):
        print(f"Subkey {i:2}: {subkey}")

if __name__ == "__main__":
    main()
