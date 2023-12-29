#**********************************************************************************************
#	Aaron Hudon
#	CS455 Cryptography and Network Security	
#	Midterm Project - TranspositionCipher.py
#	Simulation of Transposition Cipher
#**********************************************************************************************


def key_inversion(encrypt_key):
    # This is to check if the input contains exactly seven digits
    if len(encrypt_key) != 7 or not encrypt_key.isdigit() or not all(1 <= int(digit) <= 9 for digit in encrypt_key):
        raise ValueError("Invalid input.")

    encrypt_key = [int(digit) for digit in encrypt_key]

    # Create a list to store the decryption key
    decrypt_key = [0] * len(encrypt_key)

    # Create a set to keep track of used positions
    used_positions = set()

    # Iterate through the encryption key
    for i, digit in enumerate(encrypt_key):
        if digit in used_positions:
            raise ValueError("Invalid input. Duplicate digits found.")
        decrypt_key[digit - 1] = i + 1
        used_positions.add(digit)

    # Convert the decryption key back to a string
    decrypt_key_str = ' '.join(map(str, decrypt_key))

    return decrypt_key_str
# we need a while loop here to allow user to enter necessary data
# also, allow the user to go again if they would like to.
while True:
    # Get user input for the encryption key
    encrypt_key_input = input("Enter the encryption key (seven digits) :")
    # try catch block to make sure the correct values were entered, if not display error
    try:
        # Call the function to generate the decryption key
        decrypt_key = key_inversion(encrypt_key_input)
        # print statements
        print("Encryption key:", encrypt_key_input)
        print("Decryption key:", decrypt_key)
    except ValueError as e:
        print(e)

    # Ask the user if they want to try a new encryption key
    go_again = input("Do you want to try again? (yes/no): ").strip().lower()
    if go_again != "yes":
        break
