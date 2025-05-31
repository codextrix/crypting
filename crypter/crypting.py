from cryptography.fernet import Fernet
import getpass  # For secure password input

def generate_key():
    """Generate and return a Fernet key"""
    return Fernet.generate_key()

def encrypt_message(key, message):
    """Encrypt a message using the provided key"""
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

def decrypt_message(key, encrypted_message):
    """Decrypt a message using the provided key"""
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted

def main():
    # Generate or load a key
    print("1. Generate new key")
    print("2. Use existing key")
    choice = input("Choose option (1/2): ")

    if choice == '1':
        key = generate_key()
        print("\nGenerated Key (SAVE THIS SECURELY!):")
        print(key.decode())
    elif choice == '2':
        key_input = getpass.getpass("Enter your key: ").encode()
        key = key_input
    else:
        print("Invalid choice")
        return

    # Encrypt or decrypt
    print("\n1. Encrypt message")
    print("2. Decrypt message")
    operation = input("Choose operation (1/2): ")

    if operation == '1':
        message = getpass.getpass("Enter message to encrypt: ")
        encrypted = encrypt_message(key, message)
        print("\nEncrypted Message:")
        print(encrypted.decode())
    elif operation == '2':
        encrypted_message = input("Enter message to decrypt: ").encode()
        try:
            decrypted = decrypt_message(key, encrypted_message)
            print("\nDecrypted Message:")
            print(decrypted)
        except:
            print("Decryption failed! Invalid key or message")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()