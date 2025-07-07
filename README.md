# securecrypt
🔐 securecrypt-ybi-internship A command-line tool to securely encrypt and decrypt files using Python and Fernet symmetric key cryptography. Built during my 6-week internship at YBI Foundation.

# 🔐 SecureCrypt: File Encryption & Decryption Tool

A simple Python CLI-based utility to encrypt and decrypt files securely using Fernet symmetric encryption.

## ✨ Features

- 🔑 Automatically generates a secure key (`secret.key`)
- 📄 Encrypts and decrypts any file format
- ♻️ Overwrites the original files to ensure safety
- 💻 Clean and easy-to-use terminal interface
- 🛡️ Handles missing file/key and invalid decryption attempts

## 🛠️ Technologies Used

- Python 3.x
- [cryptography](https://cryptography.io/en/latest/) library (Fernet)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/securecrypt.git
cd securecrypt
```

### 2. Install Required Package

```bash
pip install cryptography
```

### 3. Run the Script

```bash
python securecrypt.py
```

Follow the prompts to:
- Create an encryption key
- Encrypt your file
- Decrypt your file

## 🔒 Important Notes

- The tool uses **Fernet** encryption (AES-128 + HMAC).
- The file `secret.key` is essential for decryption.
- Original files are overwritten—backup important data beforehand.

## 👤 Author Info

**Name**: Abhay Raj Singh  
**Institution**: YBI Foundation (Intern)

## 🔧 Future Enhancements

- GUI version using Tkinter or PyQt
- Support batch file encryption
- Password-based key generation
- Cloud upload integration

## 📚 References

- [Python Cryptography Docs](https://cryptography.io/en/latest/)
- [Fernet Spec](https://cryptography.io/en/latest/fernet/)
