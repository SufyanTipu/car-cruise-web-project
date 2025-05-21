import string

def menu():
    print("\nEncryption/Decryption Tool")
    print("1. Additive Cipher")
    print("2. Multiplicative Cipher")
    print("3. Affine Cipher")
    print("4. Hill Cipher ")
    print("5. Vigenère Cipher")
    print("6. Rotor Cipher")
    print("7. Keyed Transposition Cipher")
    print("8. Exit")

def get_choice():
    return int(input("\nSelect a cipher (1-8): "))

def additive_cipher(text, key, encrypt=True):
    shift = key if encrypt else -key
    result = ''.join(
        chr((ord(char) - 65 + shift) % 26 + 65) if char.isalpha() else char for char in text.upper()
    )
    return result

def multiplicative_cipher(text, key, encrypt=True):
    mod_inv_key = pow(key, -1, 26) if not encrypt else key
    result = ''.join(
        chr((ord(char) - 65) * mod_inv_key % 26 + 65) if char.isalpha() else char for char in text.upper()
    )
    return result

def affine_cipher(text, a, b, encrypt=True):
    mod_inv_a = pow(a, -1, 26) if not encrypt else a
    result = ''
    for char in text.upper():
        if char.isalpha():
            num = ord(char) - 65
            if encrypt:
                num = (a * num + b) % 26
            else:
                num = (mod_inv_a * (num - b)) % 26
            result += chr(num + 65)
        else:
            result += char
    return result

def hill_cipher(text, key_matrix, encrypt=True):
    n = len(key_matrix)
    text = text.upper().replace(' ', '')
    while len(text) % n != 0:
        text += 'X'  # Padding

    text_vectors = [ord(char) - 65 for char in text]
    result = ''

    for i in range(0, len(text_vectors), n):
        block = text_vectors[i:i + n]
        new_block = [0] * n
        for row in range(n):
            for col in range(n):
                new_block[row] += key_matrix[row][col] * block[col]
            new_block[row] %= 26
        result += ''.join(chr(val + 65) for val in new_block)
    return result

def vigenere_cipher(text, key, encrypt=True):
    key = key.upper()
    key_index = 0
    result = ''
    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            shift = shift if encrypt else -shift
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def rotor_cipher(text, rotors, encrypt=True):
    result = text.upper()
    for rotor in rotors:
        shift = rotor if encrypt else -rotor
        result = ''.join(
            chr((ord(char) - 65 + shift) % 26 + 65) if char.isalpha() else char for char in result
        )
    return result

def keyed_transposition_cipher(text, key, encrypt=True):
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates while preserving order
    columns = sorted(list(enumerate(key)), key=lambda x: x[1])  # Sort columns by key
    sorted_indices = [col[0] for col in columns]

    if encrypt:
        rows = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
        if len(rows[-1]) < len(key):  # Pad last row
            rows[-1] += 'X' * (len(key) - len(rows[-1]))
        result = ''.join(''.join(row[index] for index in sorted_indices) for row in rows)
    else:
        num_rows = len(text) // len(key)
        full_cols = [text[i * num_rows:(i + 1) * num_rows] for i in range(len(key))]
        reordered = [''] * len(key)
        for index, col in zip(sorted_indices, full_cols):
            reordered[index] = col
        result = ''.join(
            ''.join(reordered[col][row] for col in range(len(key))) for row in range(num_rows)
        )
    return result

if __name__ == "__main__":
    while True:
        menu()
        choice = get_choice()

        if choice == 8:
            print("Exiting the tool. Goodbye!")
            break

        text = input("\nEnter the text: ")

        if choice == 1:  # Additive Cipher
            key = int(input("Enter the key (0-25): "))
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = additive_cipher(text, key, encrypt=(mode == 'e'))

        elif choice == 2:  # Multiplicative Cipher
            key = int(input("Enter the key (must be coprime with 26): "))
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = multiplicative_cipher(text, key, encrypt=(mode == 'e'))

        elif choice == 3:  # Affine Cipher
            a = int(input("Enter 'a' (must be coprime with 26): "))
            b = int(input("Enter 'b': "))
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = affine_cipher(text, a, b, encrypt=(mode == 'e'))

        elif choice == 4:  # Hill Cipher
            size = int(input("Enter matrix size (2x2, 3x3, etc.): "))
            key_matrix = []
            print("Enter key matrix row by row (space-separated values):")
            for _ in range(size):
                key_matrix.append(list(map(int, input().split())))
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = hill_cipher(text, key_matrix, encrypt=(mode == 'e'))

        elif choice == 5:  # Vigenère Cipher
            key = input("Enter the keyword: ")
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = vigenere_cipher(text, key, encrypt=(mode == 'e'))

        elif choice == 6:  # Rotor Cipher
            rotors = list(map(int, input("Enter rotor shifts (space-separated): ").split()))
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = rotor_cipher(text, rotors, encrypt=(mode == 'e'))

        elif choice == 7:  # Keyed Transposition Cipher
            key = input("Enter the key: ")
            mode = input("Encrypt or Decrypt (e/d): ").lower()
            result = keyed_transposition_cipher(text, key, encrypt=(mode == 'e'))

        else:
            print("Invalid choice! Try again.")
            continue

        print("\nResult:", result)
