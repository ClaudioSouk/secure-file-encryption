# Secure File Encryption and Decryption System

## Overview
The **Secure File Encryption and Decryption System** is a Python-based project that demonstrates how to securely encrypt and decrypt files using the AES (Advanced Encryption Standard) algorithm. This tool is designed to protect sensitive data in text files by converting plaintext into encrypted ciphertext, which can only be decrypted with the correct key.

## Purpose
This project showcases the use of cryptography to secure sensitive information in files. It is useful for learning about encryption, data security, and the practical use of Python's `cryptography` library.

## Features
- **Key Generation**: Automatically generates a secure encryption key.
- **File Encryption**: Encrypts the content of text files using AES-256.
- **File Decryption**: Decrypts files back to their original content when provided with the correct key.
- **Error Handling**: Handles invalid keys, missing files, and invalid operations gracefully.

## Technologies Used
- **Python** (v3.8+)
- **cryptography** library

## Files
- `encrypt_decrypt.py`: Main script containing encryption and decryption logic.
- `encryption.key`: Stores the encryption key (generated during encryption).
- `example.txt`: Sample plaintext input file.
- `example_encrypted.txt`: Output file containing encrypted data.
- `example_decrypted.txt`: Output file containing decrypted data.

## How It Works
1. **Encryption**:
   - The program generates a **256-bit AES encryption key** (if not already provided).
   - It reads the contents of the plaintext file and encrypts it using the `cryptography` library.
   - The encrypted content is saved in a file with `_encrypted` appended to its name.
   - The encryption key is saved separately in a file named `encryption.key`.

2. **Decryption**:
   - The program reads the encryption key from the `encryption.key` file.
   - It decrypts the content of the encrypted file back into its original form.
   - The decrypted content is saved in a file with `_decrypted` appended to its name.

3. **Error Handling**:
   - The script checks for missing files or invalid keys.
   - It prevents overwriting existing files unless explicitly allowed.

## How to Run
1. Clone this repository to your local machine:
    ```bash
    git clone <repository_url>
    ```
2. Install the required dependencies:
    ```bash
    pip install cryptography
    ```
3. Run the script:
    ```bash
    python encrypt_decrypt.py
    ```
4. Follow the prompts to encrypt or decrypt files:
    - Provide the name of the file to encrypt or decrypt.
    - Ensure the encryption key file is present in the same directory for decryption.

## Example
### Input File (`example.txt`) 
                                 **Encryption Key**: Automatically generated and saved in `encryption.key`.
                                
### Output:
- **Encrypted File**: `example_encrypted.txt`  
Contains encrypted binary content.
- **Decrypted File**: `example_decrypted.txt`  
Contains the original text:

## License
This project is licensed under the MIT License.
