def calculateIntegrity(bits):
    # calculate if the codificated bits are a 7 bit list of lists
    if len(bits) % 7 != 0:
        raise ValueError("Input must be a list of 7 bits.")