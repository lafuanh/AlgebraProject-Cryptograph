import numpy as np


def encrypt_message(plaintext, key_matrix):
    # Define the modulo 43 alphabet
    alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
                'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26,
                '0': 27, '1': 28, '2': 29, '3': 30, '4': 31, '5': 32, '6': 33, '7': 34,
                '8': 35, '9': 36, '.': 37, ',': 38, '?': 39, '!': 40, "\n": 41, ':': 42, "'": 43}

    # Convert plaintext to uppercase
    plaintext = plaintext.upper()

    # Pad plaintext with space to make its length divisible by 3
    while len(plaintext) % 3 != 0:
        plaintext += ' '

    # Initialize the ciphertext
    ciphertext = ""

    # Iterate through the plaintext by triples of characters
    for i in range(0, len(plaintext), 3):
        # Get the numerical values of the three consecutive letters
        char1 = alphabet[plaintext[i]]
        char2 = alphabet[plaintext[i + 1]]
        char3 = alphabet[plaintext[i + 2]]

        # Convert the characters into column vectors
        vector = np.array([[char1], [char2], [char3]])

        # Encrypt the vector using the key matrix modulo 43
        encrypted_vector = np.dot(key_matrix, vector) % 44

        # Convert the encrypted vector back into characters
        encrypted_chars = [key for key, value in alphabet.items() if value == encrypted_vector[0, 0]]
        encrypted_chars.append([key for key, value in alphabet.items() if value == encrypted_vector[1, 0]][0])
        encrypted_chars.append([key for key, value in alphabet.items() if value == encrypted_vector[2, 0]][0])

        # Append the encrypted characters to the ciphertext
        ciphertext += "".join(encrypted_chars)

    return ciphertext


def decrypt_message(ciphertext, key_matrix_inv):
    # Define the modulo 43 alphabet
    alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
                'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, ' ': 26,
                '0': 27, '1': 28, '2': 29, '3': 30, '4': 31, '5': 32, '6': 33, '7': 34,
                '8': 35, '9': 36, '.': 37, ',': 38, '?': 39, '!': 40, "\n": 41, ':': 42, "'": 43}
    # Initialize the plaintext
    plaintext = ""

    # Iterate through the ciphertext by triples of characters
    for i in range(0, len(ciphertext), 3):
        # Get the numerical values of the three consecutive letters
        char1 = alphabet[ciphertext[i]]
        char2 = alphabet[ciphertext[i + 1]]
        char3 = alphabet[ciphertext[i + 2]]

        # Convert the characters into column vectors
        vector = np.array([[char1], [char2], [char3]])

        # Encrypt the vector using the key matrix modulo 43
        encrypted_vector = np.dot(np.around(key_matrix_inv), vector) % 44

        print(encrypted_vector)
        # Convert the encrypted vector back into characters
        encrypted_chars = [key for key, value in alphabet.items() if value == encrypted_vector[0, 0]]
        encrypted_chars.append([key for key, value in alphabet.items() if value == encrypted_vector[1, 0]][0])

        encrypted_chars.append([key for key, value in alphabet.items() if value == encrypted_vector[2, 0]][0])

        # Append the encrypted characters to the ciphertext
        plaintext += "".join(encrypted_chars)

    return plaintext
