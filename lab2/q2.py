# Expansion P-box Table
expansion_pbox_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

def permute(input_block, permutation_table):
    output_block = [0] * len(permutation_table)
    for i, pos in enumerate(permutation_table):
        output_block[i] = input_block[pos - 1]
    return output_block

def main():
    # Example 32-bit input block
    input_block = [
        0, 0, 1, 0, 1, 0, 1, 1,
        1, 1, 0, 0, 1, 0, 1, 0,
        0, 1, 1, 1, 1, 0, 1, 0,
        1, 0, 0, 1, 1, 1, 0, 0
    ]
    
    # Expansion Permutation
    expanded_block = permute(input_block, expansion_pbox_table)
    print("Expansion Permutation: ", expanded_block)

if __name__ == "__main__":
    main()
