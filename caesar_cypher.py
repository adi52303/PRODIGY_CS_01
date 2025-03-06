def caesar_cipher(text, shift, encrypt=True):
    result = ""
    if not encrypt:
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift) % 26)
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

# Get user input
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

if choice == 'e':
    encrypted_text = caesar_cipher(message, shift_value, encrypt=True)
    print(f"Encrypted text: {encrypted_text}")
elif choice == 'd':
    decrypted_text = caesar_cipher(message, shift_value, encrypt=False)
    print(f"Decrypted text: {decrypted_text}")
else:
    print("Invalid choice! Please enter 'E' or 'D'.")
