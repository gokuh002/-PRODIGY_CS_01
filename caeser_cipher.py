letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, shift_value):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + shift_value) % 26
                ciphertext += letters[new_index]
        else:
            ciphertext += ' '  
    return ciphertext    

def decrypt(ciphertext, shift_value):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - shift_value) % 26
                plaintext += letters[new_index]
        else:
            plaintext += ' '  
    return plaintext          

print('*******************************')
print('******** CAESAR CIPHER ********')
print('*******************************')

print()
user_input = input('DO YOU WANT TO ENCRYPT OR DECRYPT (E/D): ').upper()

if user_input == 'E':
    print('Encryption:')
    key = int(input('Enter the shift value or Key (1 to 26): '))
    text = input('Enter the text you want to Encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'D':
    print('Decryption:')
    key = int(input('Enter the shift value or key (1 to 26): '))
    text = input('Enter the text you want to Decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
