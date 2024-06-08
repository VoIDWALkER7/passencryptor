import base64

def decrypt_pass(password):
    decode_bytes = base64.b64decode((password))
    decode_data = decode_bytes.decode()
    print(f'Decoded Password:{decode_data}')

encoded_string= input("Enter the encode string:")
decrypt_pass(encoded_string)
