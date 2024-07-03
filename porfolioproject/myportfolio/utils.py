from cryptography.fernet import Fernet # type: ignore
import base64
#generamos una clave para cifrar y descifrar
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#Función cifrado de datos
def encrypt_message(message):
    cipher_text = cipher_suite.encrypt(message.encode())
    return base64.urlsafe_b64encode(cipher_text).decode()

#Función para descifrar datos
def decrypt_message(cipher_text):
    decode_cipher_text = base64.urlsafe_b64decode(cipher_text)
    decrypt_message = cipher_suite.decrypt(decode_cipher_text).decode()
    return decrypt_message


