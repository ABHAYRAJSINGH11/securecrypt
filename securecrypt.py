from cryptography.fernet import Fernet, InvalidToken
import os

KEY_FILENAME = "secret.key"

def create_encryption_key():
    """Creates a new Fernet key and stores it in a file."""
    try:
        key = Fernet.generate_key()
        with open(KEY_FILENAME, "wb") as f:
            f.write(key)
        print(f"✅ Key successfully created at: {os.path.abspath(KEY_FILENAME)}")
    except Exception as error:
        print(f"❌ Unable to generate key: {error}")
        exit(1)

def retrieve_key():
    """Reads the encryption key from the key file."""
    if not os.path.exists(KEY_FILENAME):
        print(f"❌ Key file not found at: {os.path.abspath(KEY_FILENAME)}")
        exit(1)
    with open(KEY_FILENAME, "rb") as f:
        return f.read()

def process_file(mode, path, key):
    """Encrypts or decrypts the file content based on mode."""
    try:
        absolute_path = os.path.abspath(path)
        if not os.path.isfile(absolute_path):
            raise FileNotFoundError("Target file not found.")

        cipher = Fernet(key)

        with open(absolute_path, "rb") as f:
            content = f.read()

        if mode == "encrypt":
            modified = cipher.encrypt(content)
        elif mode == "decrypt":
            modified = cipher.decrypt(content)
        else:
            raise ValueError("Unsupported operation.")

        with open(absolute_path, "wb") as f:
            f.write(modified)

        return True

    except InvalidToken:
        print("❌ Decryption failed: Invalid key or file is corrupted.")
    except Exception as error:
        print(f"❌ Error during processing: {error}")
    return False

# ----------- CLI Interaction --------------
print(f"📌 Current Directory: {os.getcwd()}")
operation = input("Type 'E' to Encrypt or 'D' to Decrypt a file: ").strip().lower()

if operation == 'e':
    file_name = input("Enter the file name to encrypt (include extension): ").strip()
    if not os.path.exists(file_name):
        print(f"❌ File does not exist: {os.path.abspath(file_name)}")
        exit(1)

    if not os.path.exists(KEY_FILENAME):
        create_encryption_key()

    key = retrieve_key()
    if process_file('encrypt', file_name, key):
        print("✅ File successfully encrypted.")
        print(f"🔐 Key saved at: {os.path.abspath(KEY_FILENAME)}")

elif operation == 'd':
    file_name = input("Enter the file name to decrypt (include extension): ").strip()
    key = retrieve_key()
    if process_file('decrypt', file_name, key):
        print("✅ File successfully decrypted.")
else:
    print("⚠️ Invalid input. Please choose either 'E' or 'D'.")
