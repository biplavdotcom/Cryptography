# S-box 1 (S1) Table
sbox1 = [
    [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
    [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
    [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
    [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
]

def sbox_substitution(input_bits, sbox):
    # Calculate row and column index for the S-box
    row = (input_bits[0] << 1) + input_bits[5]
    column = (input_bits[1] << 3) + (input_bits[2] << 2) + (input_bits[3] << 1) + input_bits[4]
    
    # Get the S-box value
    sbox_value = sbox[row][column]
    
    # Convert S-box value to 4-bit binary
    output_bits = [int(bit) for bit in f"{sbox_value:04b}"]
    return output_bits

def main():
    # Example 6-bit input block for S1
    input_block = [1, 0, 1, 1, 0, 1]  # This is just an example; any 6-bit value can be used
    
    # Apply S-box 1 substitution
    sbox1_output = sbox_substitution(input_block, sbox1)
    print("S-box 1 Output: ", sbox1_output)

if __name__ == "__main__":
    main()
