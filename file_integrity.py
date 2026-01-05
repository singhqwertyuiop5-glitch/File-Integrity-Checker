import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sha256.update(chunk)
    return sha256.hexdigest()

def save_hash(file_path, hash_value):
    with open(file_path + ".hash", "w") as f:
        f.write(hash_value)

def check_integrity(file_path):
    if not os.path.exists(file_path):
        print("❌ File does not exist.")
        return

    if not os.path.exists(file_path + ".hash"):
        print("No hash file found. Creating new hash...")
        current_hash = calculate_hash(file_path)
        save_hash(file_path, current_hash)
        print("Hash saved.")
        return

    with open(file_path + ".hash", "r") as f:
        saved_hash = f.read()

    current_hash = calculate_hash(file_path)

    if current_hash == saved_hash:
        print("✅ File integrity intact. No changes detected.")
    else:
        print("⚠️ File has been modified!")

if __name__ == "__main__":
    file_path = input("Enter file path: ")
    check_integrity(file_path)
    input("Press Enter to exit...")
