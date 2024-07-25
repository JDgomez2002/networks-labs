# Calcular checksum con fletcher16
def fletcher16(data):
    # Inicializar sumas parciales
    sum1 = 0
    sum2 = 0
    # Iterar sobre cada byte en los datos
    for byte in data:
        sum1 = (sum1 + byte) % 255
        sum2 = (sum2 + sum1) % 255
    # Combinar sum1 y sum2 para formar el checksum final
    return (sum2 << 8) | sum1

# Convertir la cadena de bits a bytes
def bits_to_bytes(bit_string: str):
    # Rellenar la cadena de bits con 0s si no es múltiplo de 8
    if len(bit_string) % 8 != 0:
        bit_string = bit_string.rjust((len(bit_string) + 7) // 8 * 8, '0')
    byte_array = bytearray()
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i+8]
        byte_array.append(int(byte, 2))
    
    return byte_array

# Convertir bytes a cadena de bits
def bytes_to_bits(byte_array):
    bit_string = ''.join(f'{byte:08b}' for byte in byte_array)
    return bit_string

# Calcular el checksum y agregarlo al final de la cadena de bits
def append_checksum(bit_string):
    data = bits_to_bytes(bit_string)
    checksum = fletcher16(data)
    checksum_bytes = checksum.to_bytes(2, 'big')  # Convertir el checksum en 2 bytes
    checksum_bits = bytes_to_bits(checksum_bytes)  # Convertir los bytes del checksum a una cadena de bits
    return bit_string + checksum_bits

# Solicitar un mensaje en binario
bit_string = input("Ingrese un mensaje en binario: ")

# Generar el mensaje con checksum
print("Calculando checksum...")
full_message = append_checksum(bit_string)
print("Listo!")
# Devolver el mensaje con checksum
print(f"Mensaje con checksum: {full_message}")
