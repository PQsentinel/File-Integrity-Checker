
import hashlib
import os

def hash_file(path):
    sha256_hash = hashlib.sha256()

    try:
        with open(path, "rb") as file:
            while True:
                chunk = file.read(4096)

                if not chunk:
                    break

                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    except OSError:
        print(f"Could not read the file: {path}")
        return None


def scan_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_hash = hash_file(file_path)

            if file_hash is not None:
                print(f"{filename}: {file_hash}")


scan_folder("test_folder")

