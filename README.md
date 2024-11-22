<<<<<<< HEAD
# Secure File Encryption and Decryption System

## Overview
This Python project demonstrates a secure file encryption and decryption system using the `cryptography` library. It showcases how sensitive data in text files can be encrypted and decrypted using a symmetric encryption algorithm.

## Features
- Generate a secure encryption key.
- Encrypt text files using the key.
- Decrypt files back to their original content with the correct key.
- Error handling for invalid keys or missing files.

## Technologies Used
- **Python** (v3.8+)
- **cryptography** library

## Files
- `encrypt_decrypt.py`: Main script for the project.
- `encryption_key.key`: File storing the encryption key.
- `example.txt`: Sample input text file.
- `example_encrypted.txt`: Encrypted file.
- `example_decrypted.txt`: Decrypted file.

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
4. Check the generated files:
    - `example_encrypted.txt`: Encrypted content.
    - `example_decrypted.txt`: Decrypted content.

## Example Output
### Input File (`example.txt`)
```
This is a sensitive piece of information that needs encryption.
```

### Encrypted File (`example_encrypted.txt`)
```
gAAAAABlX... (binary content)
```

### Decrypted File (`example_decrypted.txt`)
```
This is a sensitive piece of information that needs encryption.
```

## Future Improvements
- Add GUI for better user interaction.
- Support for encrypting/decrypting multiple files in bulk.
- Allow users to specify their encryption key.

## License
This project is licensed under the MIT License.
=======
# secure-file-encryption
A Python project demonstrating secure file encryption and decryption using the cryptography library.
>>>>>>> bfadd95ffbbe0f24c3772e19551172718185b0fa
