def encrypt_caesar(plain_text, shift):
    encrypted_text = ''
    for char in plain_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(cipher_text, shift):
    decrypted_text = ''
    for char in cipher_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char
    return decrypted_text

def show_menu():
    print("\n=== Caesar Cipher Tool ===")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted = encrypt_caesar(text, shift)
            print("Encrypted Message:", encrypted)

        elif choice == '2':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted = decrypt_caesar(text, shift)
            print("Decrypted Message:", decrypted)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
