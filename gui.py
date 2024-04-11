import math

import customtkinter as ctk
from encryption import encrypt_message
from encryption import decrypt_message
import numpy as np

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")


def generate_random_numbers():
    # Generate random numbers in the range of 1 to 255 for each entry in the key matrix
    for row_entries in matrix_entries:
        for entry in row_entries:
            entry.delete(0, ctk.END)
            entry.insert(0, np.random.randint(1, 1005))

    modulus = 44
    key = [[int(entry.get()) for entry in row] for row in matrix_entries]
    det_ = round(np.linalg.det(key))

    # Iterate over possible values of X
    for x in range(modulus):
        if (det_ * x) % modulus == 1:
            print("Found X:", x)
            break
    else:
        print("finding value")
        generate_random_numbers()


def encrypt():
    new_text = entry_message.get(1.0, "end-1c")
    key = [[int(entry.get()) for entry in row] for row in matrix_entries]


    encrypted_text = encrypt_message(new_text, key)
    # Clear previous content
    cipher_text.delete('1.0', ctk.END)
    # Insert encrypted text
    cipher_text.insert(ctk.END, encrypted_text)


def decrypt():
    cipher = cipher_text.get(1.0, "end-1c")
    key = [[int(entry.get()) for entry in row] for row in matrix_entries]

    key_matrix_inv = np.linalg.inv(key)
    det_A = round(np.linalg.det(key))
    scaled_inverse = np.dot(key_matrix_inv, det_A)

    print(key_matrix_inv)
    print(det_A)
    print(scaled_inverse)

    modulus = 44

    # Iterate over possible values of X
    for x in range(modulus):

        if (det_A * x) % modulus == 1:
            print("Found X:", x)
            # Perform the multiplication of the determinant with the scaled inverse
            inverse = x * scaled_inverse

            print(inverse)
            # Perform modulo 27 operation
            result = inverse % modulus
            decrypt_text = decrypt_message(cipher, result)
            break
    else:
        print("No solution found.")

    # Clear previous content
    plain_text.delete('1.0', ctk.END)
    # Insert encrypted text
    plain_text.insert(ctk.END, decrypt_text)


root = ctk.CTk()
root.geometry("720x580")  # width x height

root.title("Message Encryption")

label_message = ctk.CTkLabel(root, text="Enter Message:")
label_message.grid(row=0, column=0)

entry_message = ctk.CTkTextbox(root, width=400, height=100)
entry_message.grid(row=0, column=1, columnspan=2, sticky="ew", padx=20, pady=20)

label_key = ctk.CTkLabel(root, text="Enter Key (3x3 Matrix):")
label_key.grid(row=1, column=0)

matrix_entries = []
for i in range(3):
    row_entries = []
    for j in range(3):
        entry = ctk.CTkEntry(root, width=60)
        entry.grid(row=i + 2, column=j + 1)
        row_entries.append(entry)
    matrix_entries.append(row_entries)

# Button to generate random numbers in the matrix entries
generate_button = ctk.CTkButton(root, text="Generate Random Numbers", command=generate_random_numbers)
generate_button.grid(row=5, column=1, columnspan=3)

encrypt_button = ctk.CTkButton(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=6, column=1, padx=20, pady=20)

label_message = ctk.CTkLabel(root, text="Encryption Text:")
label_message.grid(row=7, column=0)
# Create a Text widget for output_label
cipher_text = ctk.CTkTextbox(root, width=400, height=90)
cipher_text.grid(row=7, column=1, columnspan=3)

label_message = ctk.CTkLabel(root, text="Decrypt Text:")
label_message.grid(row=8, column=0)
# Create a Text widget for output_label
plain_text = ctk.CTkTextbox(root, width=400, height=90)
plain_text.grid(row=8, column=1, columnspan=3, padx=10)

encrypt_button = ctk.CTkButton(root, text="Decrypt", command=decrypt)
encrypt_button.grid(row=9, column=1, padx=20, pady=20)

root.mainloop()
