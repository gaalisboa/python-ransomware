from cryptography.fernet import Fernet
import os

def load_key():
  return open("secret.key", "rb").read()

def decrypt_file(file_path, key):
  fernet = Fernet(key)
  with open(file_path, "rb") as encrypted_file:
    encrypted = encrypted_file.read()
  decrypted = fernet.decrypt(encrypted)
  with open(file_path, "wb") as decrypted_file:
    decrypted_file.write(decrypted)

def find_files_to_decrypt(directory):
  files_to_encrypt = []
  for root, _, files in os.walk(directory):
    for file in files:
      if file.endswith((".txt", ".docx", ".xlsx")):
        files_to_encrypt.append(os.path.join(root, file))
  return files_to_encrypt

key = load_key()
target_directory = "reallyImportantFiles"
files = find_files_to_decrypt(target_directory)
for file_path in files:
  decrypt_file(file_path, key)
print(f"Decrypted {len(files)} files in '{target_directory}' directory.")
