# Universidad del Valle de Guatemala
# Redes - Laboratorio 2
# Daniel Gomez 21429

# Codificate 4 bits in a 7 bit hamming code.
# @param bits: 4 bit list to codificate
# @return: 7 bit list Hamming code
def encoder(bits):
    # verify that the input is a list of 4 bits
    if len(bits) != 4:
        raise ValueError("Input must be a list of 4 bits.")
    # verify that all bits are 0 or 1
    elif any(bit not in (0, 1) for bit in bits):
        raise ValueError("Bits must be 0 or 1.")

    # assign data bits to variables
    d1, d2, d3, d4 = bits

    # Calculate parity bits
    p1 = d1 ^ d2 ^ d3 
    p2 = d1 ^ d2 ^ d4
    p3 = d1 ^ d3 ^ d4

    # Create Hamming code
    return [d1, d2, d3, p1, d4, p2, p3]

def main():
    print("\nType the transmitter message (4 bits)")
    message = input(">> ")
    bits = [int(bit) for bit in message]

    encoded = encoder(bits)

    print("------------------ Hamming algorithm ------------------")
    print("Message:", bits)
    print(f"Parity bit p1: {encoded[3]}")
    print(f"Parity bit p2: {encoded[5]}")
    print(f"Parity bit p3: {encoded[6]}")
    print(f"Parity bit p4: {encoded[4]}")
    print(f"Codificated bits: ", end="")
    for bit in encoded:
        print(bit, end="")
    print("\n--------------------------------------------------------")

if __name__ == "__main__":
    main()