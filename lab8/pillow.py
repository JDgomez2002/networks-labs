

from PIL import Image
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def process_image(input_path):
    # a. Convertir imagen a bytes usando Pillow y numpy
    img = Image.open(input_path)
    # Convertir a RGBA si no está en ese formato
    img = img.convert('RGBA')

    # Convertir a array de numpy y reshape
    img_array = np.array(img)
    img_bytes = img_array.reshape(405, 480, 4)

    # Convertir el array a bytes para el cifrado
    flat_bytes = img_bytes.tobytes()

    # b. Cifrar usando AES-128 ECB
    # Generar una clave de 16 bytes (128 bits)
    key = b'ThisIsASecretKey'  # En producción, usar una clave segura y aleatoria

    # Crear cifrador AES en modo ECB
    cipher = AES.new(key, AES.MODE_ECB)

    # Asegurar que los datos están alineados al tamaño de bloque AES (16 bytes)
    padded_data = pad(flat_bytes, AES.block_size)

    # Cifrar los datos
    encrypted_bytes = cipher.encrypt(padded_data)

    # c. Convertir bytes cifrados a imagen PNG
    # Convertir bytes cifrados a array de numpy
    # Nota: Tomamos solo los bytes necesarios para la imagen
    img_size = 405 * 480 * 4
    encrypted_array = np.frombuffer(encrypted_bytes[:img_size], dtype=np.uint8)
    encrypted_image = encrypted_array.reshape(405, 480, 4)

    # Crear imagen desde array
    encrypted_img = Image.fromarray(encrypted_image, 'RGBA')

    # Guardar como PNG
    encrypted_img.save('encrypted_tux.png')


# Ejecutar el programa
if __name__ == "__main__":
    try:
        process_image('tux.bmp')
        print("Proceso completado. Imagen cifrada guardada como 'encrypted_tux.png'")
    except FileNotFoundError:
        print("Error: No se encuentra el archivo 'tux.bmp'")
    except Exception as e:
        print(f"Error durante el proceso: {str(e)}")