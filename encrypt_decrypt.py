from cryptography.fernet import Fernet
import os

# Step 1: Generate a secure encryption key
def generate_key():
    return Fernet.generate_key()

# Step 2: Save the encryption key securely
def save_key(key, key_file):
    with open(key_file, 'wb') as f:
        f.write(key)

# Step 3: Load the encryption key
def load_key(key_file):
    if not os.path.exists(key_file):
        raise FileNotFoundError("Key file not found!")
    with open(key_file, 'rb') as f:
        return f.read()

# Step 4: Encrypt the file
def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    print(f"File '{input_file}' successfully encrypted to '{output_file}'.")

# Step 5: Decrypt the file
def decrypt_file(encrypted_file, output_file, key):
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    fernet = Fernet(key)
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("Decryption failed: Invalid key or corrupted file.")
        return
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
    print(f"File '{encrypted_file}' successfully decrypted to '{output_file}'.")

# Step 6: Test the system
if __name__ == "__main__":
    print("Welcome to Secure File Encryption System")
    key_file = "encryption_key.key"
    
    # Generate and save a key if it doesn't exist
    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key, key_file)
        print(f"Encryption key saved to '{key_file}'.")
    else:
        print(f"Encryption key found in '{key_file}'.")

    # Load the key
    key = load_key(key_file)
    
    # File paths
    input_file = "example.txt"
    encrypted_file = "example_encrypted.txt"
    decrypted_file = "example_decrypted.txt"

    # Simulating a file to encrypt
    with open(input_file, 'w') as f:
        f.write("This is a sensitive piece of information that needs encryption.")
    
    # Encrypt the file
    encrypt_file(input_file, encrypted_file, key)

    # Decrypt the file
    decrypt_file(encrypted_file, decrypted_file, key)
