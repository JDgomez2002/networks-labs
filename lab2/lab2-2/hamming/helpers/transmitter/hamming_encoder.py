
# Codificate 4 bits in a 7 bit hamming code.
# @param bits: 4 bit list to codificate
# @return: 7 bit list Hamming code

def encoder(bits):
    # bits_groups are a list of 4 bits

    if len(bits) != 4:
        raise ValueError("Input must be a list of 4 bits.")
    # verify that all bits of the 4 bit group are 0 or 1
    for bit in bits:
        if bit not in ['0', '1']:
            raise ValueError("Input must be a list of 4 bits with values 0 or 1")

    # convert the bits to integers
    bits = [int(bit) for bit in bits]

    # assign data bits to variables
    d1, d2, d3, d4 = bits

    # Calculate parity bits
    p1 = d1 ^ d2 ^ d3 
    p2 = d1 ^ d2 ^ d4
    p3 = d1 ^ d3 ^ d4

    # Create Hamming code
    return [d1, d2, d3, p1, d4, p2, p3]

def codificateMessasge(message):
    # message = "1001100111"

    # convert the message to a list of ASCII values according to the ASCII table for the characters for 0 and 1
    # ex. A = 01000001
    # To represent the letter 'A' in ASCII, the binary code 01000001 is used, which corresponds to the decimal value 65.
    message = [ord(char) for char in message]
    # convert from 65 to 8 bits
    message = [format(char, '08b') for char in message]

    bits = [int(bit) for bit in message]

    for bit in bits:
        # calculate the bit [10001] has a length of 8, if not add 0s to the left
        # bit is an integer, so convert it to a string
        if len(str(bit)) != 8:
            # replace the bit with a string of 8 bits & replace it back to the list
            completeBit = '0' * (8 - len(str(bit))) + str(bit)
            bits[bits.index(bit)] = completeBit

    # separate bits in groups of 4 length, given: ['01000001', '01000010']
    # expected: [['0100', '0001'], ['0100', '0010']] 4 bits each
    bits_groups = [[bit[i:i+4] for i in range(0, len(bit), 4)] for bit in bits]

    # codificate each group of 4 bits into a 7 bit hamming code
    # input: [['0100', '0001'], ['0100', '0010']]
    # expected: [['0100110'], ['0101101'], ['0101011'], ['0100101']]
    encoded = [[encoder(bits) for bits in bit_group] for bit_group in bits_groups]
    print(f'encoded: {encoded}')

    # concatenate all the codificated bits into a new bits list
    # input: [[['0100110'], ['0101101']], [['0101011'], ['0100101']]]
    # expected '0100110010110101011010010101'
    encoded_message = ''.join([str(bit) for bit_pair in encoded for bits in bit_pair for bit in bits])

    return encoded_message, message
