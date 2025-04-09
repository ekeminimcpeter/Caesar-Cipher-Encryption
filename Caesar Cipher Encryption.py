# Author: Ekemini Peter
# Date: December 07, 2024
# Description: Original implementation of Caesar Cipher Encryption.
# Thanks to ChatGPT for spotting a subtle error - a missing parenthesis, and robust testing of code based on scope and requirement.
# Scope: Maintain character cases and non-alphabetic characters.

##################################################################################################


# Caesar cipher.

# Collect user text and shift value
original_text = input("Enter your message to be encrypted: ")
shift_number = int(input("Enter your desired shift value from '1 and 25': "))
encrypted_text = ''

# Encrypt text according to shift value
try:                                # Check validitity of shift value.
    if shift_number in range(1,26): # Restrict user to shift range of 1–25 to ensure the encryption is both valid and non-trivial.
        for char in original_text:
            if char.isalpha():
                if char.islower():
                    encrypted_char_code = ord(char) + shift_number # Compute code word for encrypting lower case text character 
                    if encrypted_char_code > ord('z'):
                        encrypted_char_code = encrypted_char_code - 26 # Cause a cyclic encrypting on lower case letters
                elif char.isupper():
                    encrypted_char_code = ord(char) + shift_number # Compute code word for encrypting upper case text character
                    if encrypted_char_code > ord('Z'):
                        encrypted_char_code = encrypted_char_code - 26 # Cause a cyclic encryption on upper cases letters
                encrypted_text += chr(encrypted_char_code)
            else:
                encrypted_text += char
        print(encrypted_text)
    else:
        raise ValueError
    
# Manage exception error from non-valid shift value  
except ValueError:
    print("Error: shift value is invalid! Enter a value between '1 and 25'")



